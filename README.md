# Real-Time Sentiment Analysis for Any Topic on X (Twitter)

A Python tool that processes tweets and performs sentiment analysis.  
Originally designed for real-time scraping, the project now runs in offline mode using a local CSV/JSON dataset until I gain acces to X (Twitter) API.  
  
### 🚧 Temporary Change: Offline Mode Instead of Real-Time Mode  
`snscrape` broke after X (Twitter) changed their API, so live tweet fetching doesn't work right now, at least in this project.
Everything else still works fine though. Just load the tweets from a local CSV or JSON file and it's good to go. If API access becomes an option again down the line, switching back to real-time mode should be straightforward.
  
---

## Features

- Load tweets from offline CSV/JSON dataset.
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
2. Python version: Make sure you are using Python 3.11.14.
>  ⚠️ Using other versions may cause dependency issues.  
>  GitHub Codespaces comes preconfigured with 3.11.14, so you can skip this step there.

3. Create a virtual environment and install dependencies:

```bash
python3.11 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

---

## Tech Blocks

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



