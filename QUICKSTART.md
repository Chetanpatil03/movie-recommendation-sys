# 🚀 Quick Start Guide

Get your Movie Recommendation System running in 5 minutes!

## Step 1: Project Structure Setup

Create this folder structure:

```
movie-recommender/
├── app.py
├── requirements.txt
├── dataset.csv (your existing Hollywood dataset)
└── templates/
    ├── base.html
    ├── welcome.html
    ├── index.html
    ├── category.html
    ├── search.html
    ├── filter.html
    ├── movie_detail.html
    └── about.html
```

## Step 2: Install Dependencies

```bash
pip install Flask pandas scikit-learn requests
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

## Step 3: Get TMDB API Key (2 minutes)

1. Visit: https://www.themoviedb.org/signup
2. Sign up (free)
3. Go to: Settings → API → Create → Developer
4. Accept terms and fill basic info
5. Copy your API Key (v3 auth)

## Step 4: Configure Your App

Open `app.py` and update:

```python
TMDB_API_KEY = 'paste_your_api_key_here'
```

And update secret key:
```python
app.secret_key = 'change_this_to_random_string'
```

## Step 5: Run the App

```bash
python app.py
```

Open browser: http://127.0.0.1:5000/

## 🎉 That's It!

Your movie recommender is now running with Hollywood movies!

---

## ➕ Optional: Add More Datasets

### For Bollywood Movies:

1. Go to [Kaggle](https://www.kaggle.com/datasets)
2. Search "Bollywood movies dataset"
3. Download CSV
4. Rename to `bollywood.csv`
5. Place in project root folder
6. Restart app

**Recommended Dataset:**
- Search: "Indian movies dataset" or "Bollywood movies"
- Look for datasets with: title, genre, overview, rating columns

### For Web Series:

1. Go to [Kaggle](https://www.kaggle.com/datasets)
2. Search "Netflix dataset" or "TV shows dataset"
3. Download CSV
4. Rename to `webseries.csv`
5. Place in project root folder
6. Restart app

**Recommended Dataset:**
- "Netflix Movies and TV Shows"
- "TV Series Dataset"

---

## 🔧 Quick Fixes

### Posters Not Loading?
- Check your TMDB API key
- Wait a few seconds (API rate limit)

### Search Not Working?
- Make sure dataset.csv is in the root folder
- Check that 'title' and 'overview' columns exist

### Port Already in Use?
Change port in app.py:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

---

## 🎨 Quick Customization

Want to change colors? Edit `templates/base.html`:

```css
:root {
    --primary-color: #6366f1;   /* Blue */
    --secondary-color: #8b5cf6; /* Purple */
}
```

Try these color combos:
- Red/Orange: `#ef4444` and `#f97316`
- Green/Teal: `#10b981` and `#14b8a6`
- Pink/Purple: `#ec4899` and `#a855f7`

---

## 📊 Test Your Setup

After running, test these URLs:

1. Welcome page: http://127.0.0.1:5000/
2. Home: http://127.0.0.1:5000/ (after entering name)
3. Hollywood: http://127.0.0.1:5000/hollywood
4. Search: http://127.0.0.1:5000/search?q=godfather
5. Filter: http://127.0.0.1:5000/filter

All should load without errors!

---

## 🎓 For Your Presentation

**Demo Order:**
1. Welcome screen (show name input)
2. Landing page (show popular movies)
3. Search feature (search "Matrix")
4. Click a movie → show detail page
5. Show recommendations
6. Demo filter page
7. Explain algorithm briefly

**Time**: 5-7 minutes

---

## 📝 Common Questions

**Q: Do I need all three datasets?**
A: No! App works with just dataset.csv (Hollywood). Add others later.

**Q: Is TMDB API free?**
A: Yes, completely free for non-commercial use!

**Q: Can I use my own movie data?**
A: Yes! Just ensure CSV has these columns:
- title
- overview
- genre
- vote_average

**Q: How many movies can I add?**
A: No limit! But more movies = slower first load.

---

## ⚡ Performance Tips

For faster loading:
1. Limit movies in category pages (use `.head(50)`)
2. Cache TMDB API responses
3. Use smaller images from TMDB

---

## 🆘 Still Stuck?

Check:
1. ✅ Python 3.8+ installed
2. ✅ All files in correct folders
3. ✅ dataset.csv exists
4. ✅ API key is correct
5. ✅ Internet connection active

---

**Ready to impress your judges? You got this! 🚀**