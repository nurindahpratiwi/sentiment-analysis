import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.write("# Real Time Sentiment Analysis")

usr_input = st.text_input("Please rate our apps:")
nltk.download('vader_lexicon')
sentiment = SentimentIntensityAnalyzer()
score = sentiment.polarity_scores(usr_input)

if score == 0:
    st.write("Neutral")
elif score ["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")