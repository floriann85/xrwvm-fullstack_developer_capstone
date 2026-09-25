from flask import Flask
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER sentiment lexicon
nltk.download('vader_lexicon')

app = Flask(__name__)

sia = SentimentIntensityAnalyzer()


@app.route('/')
def home():
    return "Sentiment Analyzer Running"


@app.route('/analyze/<text>')
def analyze(text):
    scores = sia.polarity_scores(text)

    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)