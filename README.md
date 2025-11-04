# Real-Time Sentiment Analysis for Any Topic on X (Twitter)

A Python tool that fetches tweets on any topic and performs sentiment analysis in real-time.  
Supports multilingual sentiment detection, translation of unsupported languages via the OpenAI API, and visualization of results.

---

## Features

- Fetch tweets in real-time using `snscrape` (no API keys required).
- Clean and preprocess tweet text (remove URLs, mentions, hashtags).
- Detect language and translate unsupported languages via the OpenAI API.
- Analyze sentiment using multilingual models like RoBERTa.
- Visualize sentiment distribution with Matplotlib/Seaborn.
- Modular, easy-to-extend Python code.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AymaRehman/realtime-sentiment-analysis
cd realtime-sentiment
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Dependencies

- Python 3.8+ (recommended)
- snscrape
- pandas
- matplotlib
- seaborn
- transformers
- torch
- scipy
- langdetect
- openai 

---

## License

MIT License
