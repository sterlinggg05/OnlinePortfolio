import streamlit as st
import pandas as pd
import json

# Load Data from JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Data Visualization (Static Bar Chart) # NEW
st.subheader("Review Scores Distribution🎦")
st.bar_chart(pd.DataFrame(data["review_scores"]))

# Dynamic Graph with User Selection # NEW
st.subheader("Movie Review Ratings Over Time🎬")
chart_data = pd.DataFrame(data["review_data"])
selected_movie = st.selectbox("Select a movie:", chart_data["movie"].unique())
filtered_data = chart_data[chart_data["movie"] == selected_movie]
st.line_chart(filtered_data.set_index("year")["rating"])

# User-Interactive Slider for Dynamic Chart # NEW
st.subheader("Adjust Score Threshold💯")
score_threshold = st.slider("Select minimum score:", 0, 100, 50)
high_score_reviews = chart_data[chart_data["rating"] >= score_threshold]
st.scatter_chart(high_score_reviews.set_index("year")["rating"])

# Session State Example
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

if st.button("Increase Counter"):
    st.session_state["counter"] += 1
st.write(f"Counter: {st.session_state['counter']}")