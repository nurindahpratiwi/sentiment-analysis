from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

#DATASET
nltk.download('vader_lexicon')

#USER INPUT
usr_input = input("Please rate our apps: ")

sentiment = SentimentIntensityAnalyzer()
score = sentiment.polarity_scores(usr_input)

#CONDITION
if score == 0:
    print("Neutral")
elif score["neg"] != 0:
    print("Negative")
elif score["pos"] != 0:
    print("Positive")