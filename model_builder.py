import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

# Load Data
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

#  Merge Datasets on Title
movies = movies.merge(credits, on='title')

# Select Relevant Features
# We keep: movie_id, title, overview, genres, keywords, cast, crew
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

# Helper Parsing Functions for JSON strings
def convert(text):
    """fetch name field from JSON lists (genres, keywords)."""
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

def convert_cast(text):
    """fetch top 3 cast members."""
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
            counter += 1
    return L

def fetch_director(text):
    """fetch Director name from crew."""
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

# Apply parsers
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove Spaces to avoid token confusion (e.g. "Sam Worthington" -> "SamWorthington")
def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)

# Combine all text metadata into a single 'tags' column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id', 'title', 'tags']].copy()
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x).lower())

# Apply Stemming (e.g., "actions", "acting" -> "action")
ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])

new_df['tags'] = new_df['tags'].apply(stem)

# Vectorization (CountVectorizer / Bag of Words)
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new_df['tags']).toarray()

# Compute Cosine Similarity Matrix
similarity = cosine_similarity(vector)

print("Similarity matrix shape:", similarity.shape)

# Save Processed Artifacts
pickle.dump(new_df.to_dict(), open('movie_dict.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
print("Files saved: movie_dict.pkl and similarity.pkl")