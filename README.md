# 🎬 Movie Recommendation System

This repository contains a **Content-Based Movie Recommender System** built using:
-  Python
- 📊 Pandas, Scikit-learn
- 📚 Natural Language Processing (NLP)
- 🌐 Streamlit for web interface

It suggests similar movies based on a user-selected movie using **cosine similarity** on movie metadata like genres, keywords, cast, crew, and overview.

---

## 📌 Features

- ✅ Recommends top 5 similar movies
- ✅ Visualizes similarity scores (in notebook)
- ✅ Lightweight, fast content-based filtering
- ✅ Streamlit web interface
- ✅ Google Drive-hosted model files to bypass GitHub size limits

---

## 📁 Dataset

Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Files used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These are used to generate meaningful textual tags for movie similarity.

---

## 🧠 How It Works

1. Merges the movies and credits datasets on the movie title.
2. Extracts and combines key metadata:
   - Overview
   - Genres
   - Keywords
   - Top 3 Cast Members
   - Director (from Crew)
3. Cleans, tokenizes, and stems text data.
4. Converts movie tags into vectors using `CountVectorizer`.
5. Calculates cosine similarity between all movie pairs.
6. Saves:
   - `movie_dict.pkl`: Movie titles + tags dictionary
   - `similarity.pkl`: Cosine similarity matrix (used for recommendation)

---

## 🧪 Notebooks

### `build_model.ipynb`

- End-to-end model building notebook.
- Includes:
  - Data preprocessing
  - Feature engineering
  - Cosine similarity computation
  - Exporting model files
  - 📊 Bar plot of top 10 recommendations for a sample movie
  - Note: Make sure you have Python 3.7 or above installed.
The model files (movie_dict.pkl, similarity.pkl) will be downloaded automatically via Google Drive if not present locally.

---

## 🚀 Streamlit App

### `app.py`

An interactive web app to get movie recommendations. Built using [Streamlit](https://streamlit.io/).

#### Core Interface

```python
st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'Enter a movie name to get more recommendations',
    movies['title'].values
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    for name in names:
        st.write(name)
```
## 🛠️ Setup Instructions

Follow the steps below to run the project locally:

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
