import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()


text = "I love this product! It's amazing."
scores = analyzer.polarity_scores(text)
print(scores)