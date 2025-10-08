# 🎬 Movie Recommendation System

A comprehensive Flask-based movie recommendation system with content-based filtering, supporting Hollywood, Bollywood, and Web Series categories.

## ✨ Features

- **Smart Search**: Search across all movie categories
- **Advanced Filtering**: Filter by genre, rating, and category
- **Personalized Recommendations**: AI-powered content-based recommendations
- **Detailed Movie Information**: Cast, director, ratings, trailers, and IMDB links
- **User Session**: Personalized greeting with username
- **TMDB Integration**: Rich movie data with posters and additional details
- **Responsive Design**: Modern, mobile-friendly interface

## 🚀 Tech Stack

**Backend:**
- Flask (Python Web Framework)
- Pandas (Data Processing)
- Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- TMDB API (Movie Data)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5
- Font Awesome Icons

## 📁 Project Structure

```
movie-recommender/
│
├── app.py                      # Main Flask application
├── dataset.csv                 # Hollywood movies dataset
├── bollywood.csv              # Bollywood movies dataset (to be added)
├── webseries.csv              # Web series dataset (to be added)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
└── templates/
    ├── base.html             # Base template with navbar
    ├── welcome.html          # Welcome page with name input
    ├── index.html            # Landing page
    ├── category.html         # Hollywood/Bollywood/Web Series pages
    ├── search.html           # Search results page
    ├── filter.html           # Advanced filter page
    ├── movie_detail.html     # Movie details page
    └── about.html            # About page
```

## 📊 Dataset Requirements

### Current Dataset (dataset.csv)
Your current `dataset.csv` should have these columns:
- `id`
- `title`
- `genre`
- `original_language`
- `overview`
- `popularity`
- `release_date`
- `vote_average`
- `vote_count`

### Recommended Datasets to Add

**1. Bollywood Movies Dataset:**
- **Source**: [Kaggle - Bollywood Movies](https://www.kaggle.com/datasets)
- **Search for**: "Bollywood movies dataset" or "Indian movies dataset"
- **Required columns**: title, genre, overview, vote_average, vote_count
- **Save as**: `bollywood.csv`

**2. Web Series Dataset:**
- **Source**: [Kaggle - TV Shows/Netflix Dataset](https://www.kaggle.com/datasets)
- **Search for**: "TV series dataset" or "Netflix shows dataset"
- **Popular options**:
  - Netflix Movies and TV Shows
  - TV Shows Dataset from TMDB
- **Save as**: `webseries.csv`

**Alternative**: Use TMDB API to fetch data programmatically

## 🔧 Installation & Setup

### 1. Clone or Download the Project

```bash
# Create project directory
mkdir movie-recommender
cd movie-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get TMDB API Key

1. Go to [TMDB Website](https://www.themoviedb.org/)
2. Create a free account
3. Go to Settings → API
4. Request an API key (free for non-commercial use)
5. Copy your API key

### 4. Configure API Key

Open `app.py` and replace the API key:

```python
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'  # Replace with your actual key
```

### 5. Add Your Datasets

Place these files in the project root:
- `dataset.csv` (your existing Hollywood dataset)
- `bollywood.csv` (download from Kaggle)
- `webseries.csv` (download from Kaggle)

**Note**: If you don't have Bollywood/Web Series datasets yet, the app will still work with just Hollywood movies.

### 6. Update Dataset Loading (if needed)

If your Bollywood/Web Series datasets have different column names, update the `load_datasets()` function in `app.py`:

```python
def load_datasets():
    hollywood_df = pd.read_csv('dataset.csv')
    
    # Load Bollywood dataset
    try:
        bollywood_df = pd.read_csv('bollywood.csv')
    except FileNotFoundError:
        bollywood_df = pd.DataFrame()
    
    # Load Web Series dataset
    try:
        webseries_df = pd.read_csv('webseries.csv')
    except FileNotFoundError:
        webseries_df = pd.DataFrame()
    
    return hollywood_df, bollywood_df, webseries_df
```

## ▶️ Running the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

Open your browser and navigate to the URL.

## 📖 Usage Guide

### 1. **Welcome Page**
- Enter your name when prompted
- Name will be stored in session and displayed in navbar

### 2. **Home Page**
- View popular movies across all categories
- Use search bar to find specific movies

### 3. **Category Pages**
- **Hollywood**: Browse Hollywood movies
- **Bollywood**: Browse Bollywood movies
- **Web Series**: Browse web series

### 4. **Search**
- Search across all categories
- Real-time results as you type

### 5. **Filter Page**
- Filter by Genre (Drama, Action, Comedy, etc.)
- Filter by Minimum Rating (5.0+, 7.0+, 9.0+)
- Filter by Category (Hollywood, Bollywood, Web Series)

### 6. **Movie Detail Page**
- View complete movie information
- Watch trailers (YouTube)
- Visit IMDB page
- Get similar movie recommendations

## 🎨 Customization

### Change Color Scheme

Edit CSS variables in `templates/base.html`:

```css
:root {
    --primary-color: #6366f1;      /* Change primary color */
    --secondary-color: #8b5cf6;    /* Change secondary color */
    --dark-bg: #0f172a;            /* Change background */
    --card-bg: #1e293b;            /* Change card background */
}
```

### Modify Number of Recommendations

In `app.py`, change the `num_recommendations` parameter:

```python
recommendations = recommend_movies(movie_title, dataset, num_recommendations=8)
```

### Change Session Secret Key

For production, use a secure secret key in `app.py`:

```python
app.secret_key = 'your-secure-random-secret-key-here'
```

## 🐛 Troubleshooting

### Issue: "Movie posters not loading"
**Solution**: 
- Check your TMDB API key is correct
- Ensure you have internet connection
- TMDB has rate limits (check console for errors)

### Issue: "Bollywood/Web Series page shows 'coming soon'"
**Solution**: 
- Download and add the respective CSV files
- Ensure column names match your Hollywood dataset
- Update `load_datasets()` function if needed

### Issue: "Search returns no results"
**Solution**: 
- Check that your CSV files are loaded correctly
- Ensure movie titles are properly formatted (no extra spaces)
- Try searching with partial movie names

### Issue: "Recommendations not working"
**Solution**: 
- Ensure `overview` column exists in your dataset
- Check that the overview column has text data (not empty)
- Try with popular movies that have detailed overviews

## 📝 Dataset Format Example

Your CSV files should look like this:

```csv
id,title,genre,overview,popularity,vote_average,vote_count,release_date
278,The Shawshank Redemption,"Drama,Crime","Framed in the 1940s for...",94.075,8.7,21862,1994-09-23
```

## 🎓 For Your CLD Mini Project Competition

### Project Presentation Tips:

1. **Demo Flow**:
   - Start with welcome page → enter name
   - Show search functionality
   - Demonstrate filtering
   - Show movie detail page with recommendations
   - Explain the ML algorithm (TF-IDF + Cosine Similarity)

2. **Key Points to Highlight**:
   - Content-based filtering algorithm
   - TMDB API integration
   - Responsive design
   - User-friendly interface
   - Scalable architecture

3. **Future Enhancements** (mention during Q&A):
   - User authentication & profiles
   - Collaborative filtering
   - Movie ratings & reviews
   - Watchlist feature
   - More advanced ML models

## 📚 How the Recommendation Algorithm Works

1. **TF-IDF Vectorization**: Converts movie overviews into numerical vectors
2. **Cosine Similarity**: Calculates similarity scores between movies
3. **Ranking**: Movies with highest similarity scores are recommended
4. **Filtering**: Removes the selected movie and returns top N recommendations

```python
# Simplified algorithm
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(overviews)
similarity_scores = cosine_similarity(movie_vector, tfidf_matrix)
top_similar = similarity_scores.argsort()[-n:]
```

## 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TMDB API Documentation](https://developers.themoviedb.org/3)
- [Scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)

# codeorbit_❤️
