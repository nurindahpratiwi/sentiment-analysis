import nltk
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#DATASET
nltk.download('vader_lexicon')

#TITLE
st.title("Real Time Sentiment Analysis")

#TAKE A USER INPUT
usr_input = st.text_input("Please rate our app: ")

#PROCESS
sentiment = SentimentIntensityAnalyzer()
score = sentiment.polarity_scores(usr_input)

#CONDITION
if score["neu"] > score["neg"] and score["neu"] > score["pos"]:
    st.write("# Neutral")
elif score["neg"] > score["pos"]:
    st.write("# Negative")
else:
    st.write("# Positive")