# 📊 Dataset Resources for Movie Recommendation System

## 🎬 Hollywood Movies (You Already Have This!)

Your current `dataset.csv` is perfect! It should contain approximately 5,000 Hollywood movies with these columns:
- id, title, genre, overview, popularity, vote_average, vote_count, release_date

---

## 🇮🇳 Bollywood Movies Datasets

### Option 1: Kaggle Datasets (Recommended)

**1. Bollywood Movie Database**
- **Search on Kaggle**: "Bollywood movies dataset"
- **URL Pattern**: kaggle.com/datasets/[username]/bollywood-movies
- **What to look for**: 
  - At least 500+ movies
  - Columns: title, genre, overview, rating, year
  - Recent data (2000-2024)

**2. Indian Cinema Dataset**
- **Search**: "Indian movies dataset" or "Hindi cinema"
- **Good indicators**:
  - High upvotes/downloads
  - Recent updates
  - Clean data (few missing values)

**3. IMDb Indian Movies**
- **Search**: "IMDb Indian movies dataset"
- **Contains**: Bollywood + South Indian films
- **Filter**: You can filter to keep only Hindi films

### Option 2: TMDB API Direct Fetch

Create a Python script to fetch Bollywood movies:

```python
import requests
import pandas as pd

API_KEY = 'your_tmdb_api_key'
movies = []

# Fetch Indian movies
for page in range(1, 11):  # Get 200 movies (20 per page)
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': API_KEY,
        'with_original_language': 'hi',  # Hindi
        'sort_by': 'popularity.desc',
        'page': page
    }
    response = requests.get(url, params=params)
    movies.extend(response.json()['results'])

# Convert to DataFrame
df = pd.DataFrame(movies)
df = df.rename(columns={
    'original_title': 'title',
    'vote_average': 'vote_average'
})
df.to_csv('bollywood.csv', index=False)
```

### What to Check in Bollywood Datasets:
✅ Has 'overview' column (essential for recommendations)
✅ Has 'title' in English or transliterated Hindi
✅ Has genre information
✅ Has ratings (vote_average)
✅ Minimal missing data in overview column

---

## 📺 Web Series / TV Shows Datasets

### Option 1: Netflix Dataset (Most Popular)

**1. Netflix Movies and TV Shows**
- **Kaggle Search**: "Netflix dataset"
- **One of the best**: "Netflix Movies and TV Shows" by Shivam Bansal
- **Contains**: 8,800+ titles
- **Columns**: title, type, description, cast, country, rating
- **Perfect for**: Web series section

**2. Netflix Shows Dataset**
- **Alternative**: "netflix_titles.csv"
- **Widely used**: Many Kaggle notebooks use this
- **Clean data**: Well-maintained

### Option 2: TV Series from TMDB

**1. TV Maze Dataset**
- **Search**: "TV series dataset" on Kaggle
- **Good for**: General TV shows
- **Contains**: Popular series info

**2. IMDb TV Series**
- **Search**: "IMDb TV shows dataset"
- **Comprehensive**: Large collection
- **Format**: May need preprocessing

### Option 3: Combined Streaming Platforms

**1. Streaming Platform Dataset**
- **Search**: "streaming platforms dataset" or "OTT platforms dataset"
- **Contains**: Netflix, Prime, Hulu, Disney+
- **Benefit**: More variety

### What to Check in Web Series Datasets:
✅ Has 'overview' or 'description' column
✅ Clearly marked as TV show/series (not movies)
✅ Has title, genre, rating
✅ Recent shows included (2015-2024)
✅ Popular series present (Breaking Bad, Game of Thrones, etc.)

---

## 🔍 How to Find Datasets on Kaggle

### Step-by-Step Guide:

1. **Go to Kaggle**
   ```
   https://www.kaggle.com/datasets
   ```

2. **Search Terms to Use**:
   - "Bollywood movies"
   - "Indian cinema"
   - "Hindi movies dataset"
   - "Netflix dataset"
   - "TV series dataset"
   - "Web series dataset"
   - "OTT platform dataset"

3. **Filter Results**:
   - Sort by: "Most Downloads" or "Hotness"
   - File type: CSV
   - Check last updated date (prefer recent)

4. **Evaluate Dataset Quality**:
   - Click on dataset
   - Check "Data" tab to preview
   - Look at column names
   - Check for missing values
   - Read description and comments

5. **Download**:
   - Click "Download" button
   - Extract ZIP if needed
   - Rename to `bollywood.csv` or `webseries.csv`

---

## 📥 Quick Download Links (Most Popular)

### Kaggle Datasets (Free Account Required)

**For Bollywood:**
```
Search: "Bollywood Movie Database"
Look for datasets with 500+ movies
Download as CSV
```

**For Web Series:**
```
Dataset: "Netflix Movies and TV Shows"
Filter for type == "TV Show"
Save as webseries.csv
```

### Alternative: GitHub

Some datasets are available on GitHub:
```
github.com/search?q=bollywood+dataset+csv
github.com/search?q=netflix+dataset+csv
```

---

## 🛠️ Dataset Preprocessing

If downloaded dataset doesn't match your format, use this script:

```python
import pandas as pd

# Load downloaded dataset
df = pd.read_csv('downloaded_bollywood.csv')

# Rename columns to match your format
df = df.rename(columns={
    'movie_name': 'title',           # Adjust based on actual column names
    'description': 'overview',
    'genres': 'genre',
    'rating': 'vote_average',
    'votes': 'vote_count',
    'year': 'release_date'
})

# Add missing columns with defaults
if 'id' not in df.columns:
    df['id'] = range(1, len(df) + 1)

if 'popularity' not in df.columns:
    df['popularity'] = df['vote_count'] * df['vote_average']

# Select required columns
required_cols = ['id', 'title', 'genre', 'overview', 'popularity', 
                 'vote_average', 'vote_count', 'release_date']
df = df[required_cols]

# Save
df.to_csv('bollywood.csv', index=False)
print("Dataset prepared successfully!")
```

---

## ⚠️ Common Dataset Issues & Fixes

### Issue 1: Missing 'overview' column
**Solution**: Use 'description', 'plot', or 'summary' column
```python
df['overview'] = df['description'].fillna(df['plot'])
```

### Issue 2: Genre format different
**Solution**: Convert to comma-separated string
```python
df['genre'] = df['genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
```

### Issue 3: Missing ratings
**Solution**: Use default or fetch from TMDB API
```python
df['vote_average'] = df['vote_average'].fillna(5.0)
```

### Issue 4: Non-English characters
**Solution**: Keep them! Or transliterate if needed
```python
# Keep original titles - TMDB API handles Unicode well
```

---

## 🎯 Recommended Dataset Combinations

### Combination 1: Minimal Setup
- Hollywood: Your existing dataset.csv ✅
- Bollywood: Any 500+ movie dataset
- Web Series: Netflix top 100 shows

### Combination 2: Moderate Setup  
- Hollywood: Your existing dataset.csv ✅
- Bollywood: Comprehensive Bollywood dataset (1000+ movies)
- Web Series: Full Netflix dataset (filtered for TV shows)

### Combination 3: Complete Setup
- Hollywood: Your existing dataset.csv ✅
- Bollywood: Multiple sources combined (2000+ movies)
- Web Series: Combined streaming platforms (Netflix + Prime + Disney+)

---

## 📋 Dataset Quality Checklist

Before using a dataset, verify:

- [ ] Has at least 100+ entries
- [ ] Has 'title' column
- [ ] Has 'overview' or 'description' column (critical!)
- [ ] Has 'genre' information
- [ ] Has some form of rating/score
- [ ] CSV format (easy to load)
- [ ] Minimal missing values in 'overview' column (<10%)
- [ ] English titles or transliterated (for Bollywood)

---

## 🚀 Quick Start Without Downloading

Don't want to download datasets right now? No problem!

**Option 1**: Use the sample dataset creator
```bash
python prepare_datasets.py
# Select 'y' when asked to create sample datasets
```

This creates small sample datasets (5 movies each) so you can:
- Test the app immediately
- Understand the required format
- Replace with real datasets later

**Option 2**: Start with Hollywood only
- Your app works perfectly with just `dataset.csv`
- Add other datasets later when you find good ones

---

## 📚 Additional Resources

### Dataset Sources:
1. **Kaggle**: https://www.kaggle.com/datasets
2. **UCI ML Repository**: https://archive.ics.uci.edu/ml/datasets.php
3. **GitHub**: Search for "movie dataset csv"
4. **Data.world**: https://data.world/datasets/movies

### TMDB API:
- **API Docs**: https://developers.themoviedb.org/3
- **Get API Key**: https://www.themoviedb.org/settings/api
- **Rate Limits**: 40 requests per 10 seconds (free tier)

### Preprocessing Tools:
- **Pandas**: Data cleaning and manipulation
- **OpenRefine**: GUI tool for cleaning messy data
- **csvkit**: Command-line CSV toolkit

---

## 💡 Pro Tips

1. **Start Small**: Begin with 100-200 movies per category
2. **Quality > Quantity**: Better to have 500 good entries than 5000 bad ones
3. **Check Overview**: This column is CRITICAL for recommendations
4. **Test Early**: Load dataset and test app before competition
5. **Backup Plan**: Keep sample datasets as fallback

---

## ✅ Final Checklist

Before competition day:

- [ ] Downloaded Bollywood dataset
- [ ] Downloaded Web Series dataset
- [ ] Verified all CSVs load without errors
- [ ] Tested recommendations work on all categories
- [ ] Checked for missing 'overview' values
- [ ] Renamed files correctly (bollywood.csv, webseries.csv)
- [ ] Ran `python prepare_datasets.py` to validate

---

**Need help finding datasets? Search these exact terms on Kaggle:**

1. "Bollywood Movie Dataset"
2. "Netflix Movies and TV Shows"
3. "Indian Cinema Database"
4. "TV Series Dataset TMDB"

**Good luck! 🎬**