```markdown
# 🎬 Movie Recommender System

A Content-Based Movie Recommender System and interactive web application built with **Python**, **Scikit-Learn**, and **Streamlit** using the **TMDB 5000 Movie Dataset**. 

The system processes movie metadata (genres, keywords, cast, crew, and plot summaries), converts textual descriptions into high-dimensional vector representations using **CountVectorizer / Bag of Words**, and calculates pairwise similarities using **Cosine Similarity** to recommend the top 5 most relevant films alongside live posters via the TMDB API.

---

## 🛠️ Key Features

- **Metadata Preprocessing & Feature Fusion:** Extracts and combines key attributes (plot summary, top 3 actors, director, genres, and keywords) into a consolidated `tags` column.
- **Natural Language Processing (NLP):** Applies token normalization, stop-word filtering, and Porter Stemming to standardize keyword roots.
- **Vector Space Modeling:** Computes a 5,000-feature vector space to calculate **Cosine Similarity** scores across 4,800+ movies.
- **Live Poster Fetching:** Connects to The Movie Database (TMDB) API to retrieve high-resolution movie posters dynamically.
- **Interactive Web Interface:** Streamlit-powered UI allowing real-time search and recommendations.

---

## 📂 Repository Structure

```text
├── .vscode/                 # Editor configuration files
├── tmdb_5000_movies.csv     # TMDB Movie Metadata Dataset
├── tmdb_5000_credits.csv    # TMDB Credits Dataset (Cast & Crew)
├── model_builder.py         # Data processing & similarity matrix builder
├── movie_dict.pkl           # Serialized movie dictionary artifact
├── similarity.pkl           # Serialized cosine similarity matrix
├── app.py                   # Streamlit live web application
└── README.md                # Project documentation

```

---

## 🚀 How to Clone & Run Locally

### 1. Prerequisites

Ensure you have **Python 3.8+** and **Git** installed on your machine.

---

### 2. Clone the Repository

```bash
git clone (https://github.com/NajeebAhmed69/Movie_Recommended_System_ML_Project.git)

```

---

### 3. Create & Activate a Virtual Environment

* **Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate

```


* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



---

### 4. Install Dependencies

```bash

```

*(run: `pip install streamlit pandas numpy scikit-learn nltk requests`)*

---

### 5. Build the Recommendation Model Artifacts

Before launching the web app, run `model_builder.py` once to preprocess the raw CSV datasets and generate `movie_dict.pkl` and `similarity.pkl`:

```bash
python model_builder.py

```

---

### 6. Launch the Streamlit Web Application

Run the following command in your terminal:

```bash
streamlit run app.py

```

Streamlit will automatically open the application in your browser at:
👉 **`http://localhost:8501`**

---

## 💻 How It Works

1. Select or search for any movie from the dropdown menu (e.g., *Avatar*, *The Dark Knight Rises*, *Inception*).
2. Click **"Get Recommendations"**.
3. The application ranks movies by cosine similarity score and displays the **Top 5 recommended movies** along with their official poster artwork.

---

## 📊 Dataset Reference

* **Source:** [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Files:** `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`

---

## 📄 License

Distributed under the MIT License. Feel free to modify and adapt this project for portfolio and learning purposes.

```

```