# Sentiment analysis using RoBERTa Twitter model
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
LABELS = ["negative", "neutral", "positive"]


def analyze_sentiment(cleaned_tweets, batch_size=8):
    """
    Analyze the sentiment of preprocessed tweet content using batch processing.

    Parameters:
        cleaned_tweets (list): List of dicts with keys 'id', 'username', 'date', 'cleaned_content'
        batch_size (int): Number of tweets to process at once

    Returns:
        list: List of dicts including 'sentiment' and 'sentiment_score'
    """
    results = []

    # Prepare texts; replace empty strings with placeholder to avoid tokenizer errors
    texts = [
        t["cleaned_content"] if t["cleaned_content"].strip() else "[EMPTY]"
        for t in cleaned_tweets
    ]

    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i : i + batch_size]

        # Tokenize the batch
        inputs = tokenizer(
            batch_texts, return_tensors="pt", padding=True, truncation=True
        )

        with torch.no_grad():
            logits = model(**inputs).logits

        probs = torch.softmax(logits, dim=1).numpy()

        for j, prob in enumerate(probs):
            label_index = int(np.argmax(prob))
            sentiment_label = LABELS[label_index]
            sentiment_score = float(prob[label_index])

            # If original tweet was empty, force neutral
            orig_tweet = cleaned_tweets[i + j]
            if orig_tweet["cleaned_content"].strip() == "":
                sentiment_label = "neutral"
                sentiment_score = 0.0

            results.append(
                {
                    **orig_tweet,
                    "sentiment": sentiment_label,
                    "sentiment_score": sentiment_score,
                }
            )

    return results
