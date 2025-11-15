# Fetch tweets from a local CSV or JSON file (temporary offline mode)
# because I do not have access to X/Twitter or its API at the moment.

# Import necessary libraries
import pandas as pd  # For handling CSV files and DataFrame manipulation
import json  # For handling JSON data
import os  # For checking if the file exists


def fetch_tweets(source, limit=50, save_to_json=False):
    """
    Load tweets from a local CSV or JSON dataset.

    Parameters:
        source (str): The file path to the CSV or JSON file containing tweets.
        limit (int): The maximum number of tweets to load. Defaults to 50.
        save_to_json (bool): This parameter is not used in offline mode. It is kept for compatibility.

    Returns:
        tweets_list (list): A list of dictionaries, where each dictionary represents a tweet.
    """

    # Check if the provided source file exists
    if not os.path.isfile(source):
        raise FileNotFoundError(f"File not found: {source}")

    # Extract the file extension to determine the format (CSV or JSON)
    ext = source.split(".")[-1].lower()

    # Load data from JSON file
    if ext == "json":
        with open(
            source, "r", encoding="utf-8"
        ) as f:  # utf-8 encoding to handle special characters
            data = json.load(f)

    # Load data from CSV file
    elif ext == "csv":
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(source)
        # Convert the DataFrame into a list of dictionaries (one for each tweet)
        data = df.to_dict(orient="records")

    else:
        # Raise an error if the file format is unsupported
        raise ValueError("Unsupported file format. Use CSV or JSON.")

    # Prepare a list to store the tweets (dictionaries)
    tweets_list = []

    # Iterate over the data (up to the 'limit' number of tweets)
    for row in data[:limit]:
        # For each row (tweet), extract relevant information into a dictionary
        tweet = {
            "date": row.get(
                "date", ""
            ),  # Get the tweet date, defaulting to an empty string if not available
            "id": row.get(
                "id", ""
            ),  # Get the tweet ID, defaulting to an empty string if not available
            "content": row.get(
                "content", ""
            ),  # Get the tweet content, defaulting to an empty string if not available
            "username": row.get(
                "username", ""
            ),  # Get the username of the tweet author, defaulting to an empty string if not available
        }
        tweets_list.append(tweet)  # Add the tweet to the list

    # Print how many tweets were loaded from the file
    print(f"Loaded {len(tweets_list)} tweets from {source}")

    # Return the list of tweet dictionaries
    return tweets_list
