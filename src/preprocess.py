import re  # Regular expressions for text cleaning (is a python built-in library)
import nltk  # Natural Language Toolkit for text processing
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download NLTK resources (run once)
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("stopwords", quiet=True)


def clean_tweet(text):
    """
    Clean a single tweet:
    - Remove URLs, mentions, hashtags, emojis
    - Lowercase
    - Remove punctuation
    """
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.lower().strip()


def preprocess_tweets(tweets_list):
    """
    Preprocess a list of tweets:
    - Clean text
    - Tokenize
    - Lemmatize
    - Remove stopwords
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    cleaned_tweets = []
    for tweet in tweets_list:
        text = clean_tweet(tweet.get("content", ""))

        if not text:  # minimal change: skip empty tweets early
            cleaned_text = ""
        else:
            tokens = word_tokenize(text)
            tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
            cleaned_text = " ".join(tokens)

        cleaned_tweets.append(
            {
                "id": tweet.get("id", ""),
                "username": tweet.get("username", ""),
                "date": tweet.get("date", ""),
                "cleaned_content": cleaned_text,
            }
        )

    return cleaned_tweets
