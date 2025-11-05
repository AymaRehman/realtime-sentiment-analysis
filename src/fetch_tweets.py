# import necessary libraries
# using snscrape to fetch tweets from X/Twitter because: it does not require API keys
# and I do not have access to X/Twitter

import snscrape.modules.twitter as sntwitter  # Tool to scrape tweets from X/Twitter
import pandas as pd                           # For storing data in table format (dataframes)
import json                                   # To save data as JSON file

def fetch_tweets(topic, limit=50, save_to_json=True):
    """
    Fetch tweets containing the topic keyword.
    
    Parameters:
        topic (str): Keyword or hashtag to search for.
        limit (int): Maximum number of tweets to fetch. (limited to 50 for performance)
        save_to_json (bool): Whether to save fetched tweets to a JSON file or not.
    
    Returns:
        tweets_list (list): A list of tweet texts.
    """

    # List to store tweets
    tweets_list = []

    # Scrape tweets using snscrape
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(topic).get_items()):
        if i >= limit:  # Stop after reaching the limit
            break
        tweets_list.append({
            "date": str(tweet.date),
            "id": tweet.id,
            "content": tweet.content,
            "username": tweet.user.username
        })

    # Optionally save tweets to JSON
    if save_to_json:
        with open(f"data/{topic}_tweets.json", "w", encoding="utf-8") as f:
            # utf-8 encoding to handle special characters (non-ASCII characters)
            json.dump(tweets_list, f, ensure_ascii=False, indent=4)
            # ensure_ascii=False to preserve special characters

    print(f"Fetched {len(tweets_list)} tweets about '{topic}'")
    return tweets_list