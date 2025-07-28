# 🎬 Movie Mood Recommender

Feeling nostalgic? God-mode? Just got ghosted and need comfort cinema?  
This app gets your vibe — and gives you movie recs to match. Built with ML + Streamlit.  

---

## 🧠 What It Does

You type your current mood (e.g. “chaotic”, “lonely”, “feeling main character”)  
→ it returns 3 movie recommendations based on vibe similarity.

- Built using **K-Nearest Neighbors (KNN)** algorithm
- Vectorized mood tags using **TfidfVectorizer**
- 20 movies with custom vibes, tags, and genres
- Fast + interactive UI with **Streamlit**

---

## 🎨 Example
 <img width="1708" height="887" alt="Screenshot 1947-05-06 at 10 43 00 PM" src="https://github.com/user-attachments/assets/0e746bc2-7a19-46ab-9a2a-72546ff900d0" />

---

## 🛠️ Tech Stack

- Python
- scikit-learn
- pandas
- Streamlit

---

## 🧩 How It Works

1. Takes user mood input
2. Vectorizes mood + all movie tags using `TfidfVectorizer`
3. Runs cosine similarity to find the closest tag matches
4. Returns top `k` movies with matching vibes

---

## 📁 Project Structure

├── app.py                # Streamlit UI
├── knn_recommender.py    # ML logic
├── movies.csv            # Dataset with 20 movies

