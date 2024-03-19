from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text = "I love this product! It's amazing."
scores = analyzer.polarity_scores(text)
print(scores)