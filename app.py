import streamlit as st
from scraper import scrape_tweets
from sentiment import analyze_sentiment
import pandas as pd

st.title("🧠 Twitter Brand Mention & Sentiment Analyzer")

brand = st.text_input("Enter a brand name to search", "Nike")
max_tweets = st.slider("Max number of tweets", 10, 500, 100)

if st.button("Scrape and Analyze"):
    with st.spinner("Scraping tweets..."):
        df = scrape_tweets(brand, max_tweets=max_tweets)

    if not df.empty:
        with st.spinner("Analyzing sentiment..."):
            sentiments = analyze_sentiment(df['content'].tolist())
            df['label'] = [s['label'] for s in sentiments]
            df['score'] = [s['score'] for s in sentiments]

        st.success(f"{len(df)} tweets analyzed.")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, f"{brand}_tweets.csv", "text/csv")
    else:
        st.warning("No tweets found.")
