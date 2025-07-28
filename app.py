import streamlit as st
from knn_recommender import KNNMovieRecommender

# Streamlit app starts here
st.set_page_config(page_title="🎬 Movie Mood Recommender", layout="centered")

# Custom CSS for background and styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/c1/82/27/c18227c5761481b1554c905cd55bcc1e.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }

    .main > div {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }

    input[type="text"], .stTextInput > div > div > input {
        color: black !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid white !important;
    }

    ::placeholder {
        color: #f5f5f5 !important;
        opacity: 1 !important;
    }

    label, .stTextInput label {
        color: #ADD8E6 !important;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🎬 Movie Mood Recommender")
st.caption("Vibe → Match → Watch 🍾")

# Mood input
mood_input = st.text_input("💭 What Type of Movie u wanna binge watch?", placeholder="e.g. nostalgic, stressed, slay-mode")

# If mood entered, generate recommendations
if mood_input:
    recommender = KNNMovieRecommender()
    recs = recommender.recommend_movies(mood_input)

    st.subheader("🎯 Based on your vibe, watch these:")
    for _, row in recs.iterrows():
        st.markdown(f"**🎥 {row['Movie']}** — _{row['Tags']}_")

# Footer
st.markdown("---")
st.markdown("✨ Built with Streamlit + ML by [@shreehanna](https://github.com/shreehanna)")
