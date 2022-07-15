from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

#DOWNLOAD DATASET
nltk.download('vader_lexicon')

#INPUT USER
user_input = input ("Please rate our Apps: ")

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(user_input)

#CONDITION
if score["neg"] != 0:
    print("Negative")
else:
    print("Positive")