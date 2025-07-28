import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class KNNMovieRecommender:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "mood_movie_data.csv")
        print("📂 CSV path:", file_path)  # Debug print
        self.data = pd.read_csv(file_path)

        self.vectorizer = CountVectorizer()
        self.mood_matrix = self.vectorizer.fit_transform(self.data['Tags'])

    def recommend_movies(self, mood_input):
        input_vec = self.vectorizer.transform([mood_input])
        similarity = cosine_similarity(input_vec, self.mood_matrix)
        top_indices = similarity[0].argsort()[-3:][::-1]
        return self.data.iloc[top_indices][['Movie', 'Tags']]
