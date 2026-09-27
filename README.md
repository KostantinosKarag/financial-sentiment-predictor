# Financial Sentiment & Stock Trend Predictor

An AI-powered application that combines financial news sentiment analysis with historical stock data to analyze and predict stock market trends.

---

## Key Features
- **Stock Data Retrieval:** Automatically fetches historical market data using `yfinance`.
- **Financial NLP & Sentiment Analysis:** Evaluates financial news headlines using custom lexicon-enhanced VADER sentiment analysis.
- **Machine Learning Model:** Features a Random Forest Classifier trained on technical indicators (Moving Averages, Volatility, Daily Returns).
- **Interactive Web Dashboard:** Built with Streamlit for real-time data visualization and interactive analysis.

---

## Tech Stack & Libraries
- **Language:** Python 3.9+
- **Data & ML:** Pandas, NumPy, Scikit-Learn
- **NLP:** NLTK (VADER Sentiment Analysis)
- **Finance API:** `yfinance`
- **Web Interface:** Streamlit

---

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/KostantinosKarag/financial-sentiment-predictor.git](https://github.com/KostantinosKarag/financial-sentiment-predictor.git)
   cd financial-sentiment-predictor