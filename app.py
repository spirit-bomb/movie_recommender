import streamlit as st
import pickle
import pandas as pd
import os
import gdown

# Google Drive File IDs
movie_dict_id = '18F0D8TiLhmkEomfiM82xfG0YNd3PPSxD'
similarity_id = '1Sd67yDj9eVmiKuWh5jOsGYsLGsyckOvl'

# Download if not already present
if not os.path.exists('movie_dict.pkl'):
    gdown.download(f'https://drive.google.com/uc?id={movie_dict_id}', 'movie_dict.pkl', quiet=False)

if not os.path.exists('similarity.pkl'):
    gdown.download(f'https://drive.google.com/uc?id={similarity_id}', 'similarity.pkl', quiet=False)

# Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender')

selected_movie_name = st.selectbox('Enter a movie name to get more recommendations', movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    for j in names:
        st.write(j)
