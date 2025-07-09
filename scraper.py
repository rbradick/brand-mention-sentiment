import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(brand, max_tweets=100, since="2023-01-01"):
    query = f"{brand} since:{since}"
    tweets = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append({
            "date": tweet.date,
            "user": tweet.user.username,
            "content": tweet.content,
            "url": tweet.url
        })

    return pd.DataFrame(tweets)
