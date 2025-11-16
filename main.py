# main.py
import json
import os
import pandas as pd

# Import required modules
from src.fetch_tweets import fetch_tweets
from src.preprocess import preprocess_tweets
from src.analyze_sentiment import analyze_sentiment
from src.visualize import visualize_all

# -------------------------------
# Configuration
# -------------------------------
DATA_FOLDER = "data"
INPUT_FILE = os.path.join(DATA_FOLDER, "sample_tweets.json")
CLEAN_FILE = os.path.join(DATA_FOLDER, "clean_tweets.csv")
SENTIMENT_FILE = os.path.join(DATA_FOLDER, "sentiment_tweets.csv")

TWEET_LIMIT = None  # None means process all tweets in the file
BATCH_SIZE = 8  # minimal change: batch size for sentiment analysis


# -------------------------------
# Main pipeline
# -------------------------------
def main():
    print("\n[1/4] Loading tweets from JSON...")

    if not os.path.exists(INPUT_FILE):
        print(f"[ERROR] Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        tweets_list = json.load(f)

    if TWEET_LIMIT:
        tweets_list = tweets_list[:TWEET_LIMIT]

    print(f"[INFO] Loaded {len(tweets_list)} tweets.")

    # -------------------------------
    # Preprocess tweets
    # -------------------------------
    print("\n[2/4] Preprocessing tweets...")
    cleaned_tweets = preprocess_tweets(tweets_list)

    # Save cleaned tweets to CSV
    df_clean = pd.DataFrame(cleaned_tweets)
    df_clean.to_csv(CLEAN_FILE, index=False, encoding="utf-8")
    print(f"[INFO] Cleaned tweets saved to: {CLEAN_FILE}")

    # -------------------------------
    # Sentiment analysis
    # -------------------------------
    print("\n[3/4] Analyzing sentiment...")
    sentiment_results = analyze_sentiment(
        cleaned_tweets, batch_size=BATCH_SIZE
    )  # minimal change

    # Save sentiment results to CSV
    df_sentiment = pd.DataFrame(sentiment_results)
    df_sentiment.to_csv(SENTIMENT_FILE, index=False, encoding="utf-8")
    print(f"[INFO] Sentiment results saved to: {SENTIMENT_FILE}")

    # -------------------------------
    # Visualizations
    # -------------------------------
    print("\n[4/4] Generating visualizations...")
    visualize_all(df_sentiment)

    print("\n[✓] Pipeline completed successfully!")


# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    main()
