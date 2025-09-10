import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


API_KEY = "41e6a6fc"

def load_data():
    return pd.read_csv("dataset.csv") 

movies_df = load_data()


def recommend_movies(movie_title, num_recommendations=7):
    if movie_title not in movies_df['title'].values:
        return []

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies_df['overview'].fillna(""))

    movie_idx = movies_df[movies_df['title'] == movie_title].index[0]
    similarity_scores = cosine_similarity(tfidf_matrix[movie_idx], tfidf_matrix).flatten()

    similar_movies_idx = similarity_scores.argsort()[-(num_recommendations + 1):-1][::-1]
    return movies_df.iloc[similar_movies_idx]['title'].tolist()


def get_movie_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "True":
            return data.get("Poster")
        else:
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None


st.title("🎬 Movie Recommendation System")

movie_title = st.selectbox("Choose a Movie", movies_df['title'].unique())

if st.button("Get Recommendations"):
    recommended_movies = recommend_movies(movie_title)
    
    if recommended_movies:
        st.subheader("🔥 Recommended Movies:")
        cols = st.columns(7)  

        for i, rec_movie in enumerate(recommended_movies):
            with cols[i % 7]:  
                poster_url = get_movie_poster(rec_movie)
                if poster_url:
                    st.image(poster_url, caption=rec_movie, use_container_width=True)
                else:
                    st.write(rec_movie) 
