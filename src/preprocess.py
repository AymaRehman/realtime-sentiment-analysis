import re # Regular expressions for text cleaning (is a python built-in library)
import nltk # Natural Language Toolkit for text processing
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download NLTK resources (run once)
nltk.download('punkt', quiet=True)  # Punkt tokenizer models for sentence and word tokenization
nltk.download('wordnet', quiet=True)  # WordNet lexical database for word lemmatization and meaning or definitions
nltk.download('stopwords', quiet=True)  # A list of common stopwords for text filtering (e.g., "the", "is", "and")

def clean_tweet(text):
    """
    Clean a single tweet:
    - Remove URLs, mentions, hashtags, emojis
    - Lowercase
    - Remove punctuation
    """
    text = re.sub(r"http\S+", "", text)           # Remove URLs, \s+ means one or more non-whitespace characters
    text = re.sub(r"@\w+", "", text)              # Remove mentions, \w+ means one or more word characters (letters, digits, or underscores)
    text = re.sub(r"#\w+", "", text)              # Remove hashtags
    text = re.sub(r"[^\w\s]", "", text)           # Remove punctuation, ^ means everything except word characters and whitespace
    text = text.lower()                           # Lowercase
    text = text.strip()                           # Remove extra spaces
    return text

def preprocess_tweets(tweets_list):
    """
    Preprocess a list of tweets:
    - Clean text
    - Tokenize
    - Lemmatize
    - Remove stopwords
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    cleaned_tweets = []
    for tweet in tweets_list:
        text = clean_tweet(tweet['content'])
        tokens = word_tokenize(text)
        tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
        cleaned_text = " ".join(tokens)
        cleaned_tweets.append({
            'id': tweet['id'],
            'username': tweet['username'],
            'date': tweet['date'],
            'cleaned_content': cleaned_text
        })
    return cleaned_tweets
