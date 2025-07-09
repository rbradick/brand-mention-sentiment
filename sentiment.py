from transformers import pipeline

def analyze_sentiment(texts):
    sentiment_pipeline = pipeline("sentiment-analysis")
    results = sentiment_pipeline(texts)
    return results
