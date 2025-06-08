import streamlit as st
import pickle
import pandas as pd
import os
import gdown


@st.cache_resource
def load_data():
    # Google Drive File IDs
    movie_dict_id = '18F0D8TiLhmkEomfiM82xfG0YNd3PPSxD'
    similarity_id = '1Sd67yDj9eVmiKuWh5jOsGYsLGsyckOvl'

    # Download files if they don't exist
    if not os.path.exists('movie_dict.pkl'):
        with st.spinner('Downloading movie dictionary...'):
            gdown.download(
                f'https://drive.google.com/uc?id={movie_dict_id}',
                'movie_dict.pkl',
                quiet=False
            )

    if not os.path.exists('similarity.pkl'):
        with st.spinner('Downloading similarity matrix...'):
            gdown.download(
                f'https://drive.google.com/uc?id={similarity_id}',
                'similarity.pkl',
                quiet=False
            )

    try:
        movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return movies, similarity
    except (EOFError, FileNotFoundError) as e:
        # If files are corrupted, remove them and retry download
        if os.path.exists('movie_dict.pkl'):
            os.remove('movie_dict.pkl')
        if os.path.exists('similarity.pkl'):
            os.remove('similarity.pkl')
        st.error('Error loading files. Please refresh the page to retry download.')
        st.stop()


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load the data
movies, similarity = load_data()

# Streamlit UI
st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'Enter a movie name to get more recommendations',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Getting recommendations...'):
        names = recommend(selected_movie_name)
        for j in names:
            st.write(j)