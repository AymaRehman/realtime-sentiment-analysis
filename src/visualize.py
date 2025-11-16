import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import matplotlib.dates as mdates

plt.style.use("ggplot")  # built-in, modern clean style

COLOR_MAP = {"positive": "#2ca02c", "neutral": "#7f7f7f", "negative": "#d62728"}


def plot_sentiment_distribution(df):
    sentiment_counts = Counter(df["sentiment"])
    plt.figure(figsize=(8, 5))
    colors = [COLOR_MAP[s] for s in sentiment_counts.keys()]
    bars = plt.bar(
        sentiment_counts.keys(),
        sentiment_counts.values(),
        color=colors,
        edgecolor="black",
        width=0.6,
    )

    # Add value labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.2,
            int(yval),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.title("Sentiment Distribution", fontsize=14, weight="bold")
    plt.xlabel("Sentiment", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("data/sentiment_distribution_bar.png")
    plt.close()
    print("[INFO] Sentiment bar chart saved to data/sentiment_distribution_bar.png")


def plot_sentiment_pie(df):
    sentiment_counts = Counter(df["sentiment"])
    colors = [COLOR_MAP[s] for s in sentiment_counts.keys()]
    plt.figure(figsize=(7, 7))
    plt.pie(
        sentiment_counts.values(),
        labels=sentiment_counts.keys(),
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        explode=[0.05] * len(sentiment_counts),  # slightly explode slices
        shadow=True,
    )
    plt.title("Sentiment Proportion", fontsize=14, weight="bold")
    plt.axis("equal")  # keeps the pie circular
    plt.tight_layout()
    plt.savefig("data/sentiment_proportion_pie.png")
    plt.close()
    print("[INFO] Sentiment pie chart saved to data/sentiment_proportion_pie.png")


def plot_sentiment_over_time(df):
    if "date" not in df.columns:
        print("[NOTE] No 'date' column found. Skipping time-series plot.")
        return

    try:
        df["date"] = pd.to_datetime(df["date"])
    except Exception:
        print("[NOTE] Unable to convert 'date' column to datetime. Skipping.")
        return

    trend_df = (
        df.groupby([df["date"].dt.date, "sentiment"]).size().unstack(fill_value=0)
    )
    plt.figure(figsize=(10, 6))

    for sentiment in trend_df.columns:
        plt.plot(
            trend_df.index,
            trend_df[sentiment],
            label=sentiment.capitalize(),
            marker="o",
            linewidth=2,
            markersize=6,
            color=COLOR_MAP.get(sentiment, "black"),
        )

    plt.title("Sentiment Trend Over Time", fontsize=14, weight="bold")
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Tweet Count", fontsize=12)
    plt.legend(title="Sentiment")
    plt.grid(True, linestyle="--", alpha=0.3)

    # Format x-axis for better readability
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("data/sentiment_trend_over_time.png")
    plt.close()
    print(
        "[INFO] Sentiment time-series chart saved to data/sentiment_trend_over_time.png"
    )


def visualize_all(df):
    print("\n[+] Generating sentiment bar chart...")
    plot_sentiment_distribution(df)
    print("\n[+] Generating sentiment pie chart...")
    plot_sentiment_pie(df)
    print("\n[+] Generating sentiment time-series chart (if possible)...")
    plot_sentiment_over_time(df)
