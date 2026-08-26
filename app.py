import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Helper function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    try:
        # Free public TMDB API endpoint
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Load saved model data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    
    recommended_names = []
    recommended_posters = []
    
    # Top 5 most similar movies
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_names, recommended_posters

st.title("🎬 Movie Recommended System")
st.write("Select a movie to discover top 5 most similar films based on genres and cast.")

selected_movie = st.selectbox(
    "Choose a movie name:",
    movies['title'].values
)

if st.button("Get Recommendations"):
    names, posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
            