import streamlit as st
import pandas as pd
from fetch_data import fetch_stock_data
from sentiment_analysis import analyze_financial_sentiment

# Τίτλος εφαρμογής
st.set_page_config(page_title="AI Financial Predictor", layout="wide")
st.title("📈 Financial Sentiment & Stock Trend Predictor")
st.markdown("An AI tool combining stock price trends with news sentiment analysis.")

# Sidebar για παραμέτρους
st.sidebar.header("User Options")
ticker = st.sidebar.text_input("Stock Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-01-01"))

# 1. Εμφάνιση Δεδομένων Μετοχής
st.subheader(f"📊 Historical Data for {ticker.upper()}")
data = fetch_stock_data(ticker, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

if data is not None and not data.empty:
    st.line_chart(data['Close'])
    
    with st.expander("Show Raw Data Table"):
        st.dataframe(data)

# 2. Ανάλυση Συναισθήματος Ειδήσεων
st.subheader("📰 Financial News Sentiment Analyzer")
user_news = st.text_area(
    "Enter a financial news headline to analyze:", 
    value="NVIDIA launches new AI chip, beating all market expectations."
)

if st.button("Analyze Sentiment"):
    results = analyze_financial_sentiment([user_news])
    item = results[0]
    
    if item['sentiment'] == "POSITIVE":
        st.success(f"**Sentiment:** {item['sentiment']} (Score: {item['score']})")
    elif item['sentiment'] == "NEGATIVE":
        st.error(f"**Sentiment:** {item['sentiment']} (Score: {item['score']})")
    else:
        st.info(f"**Sentiment:** {item['sentiment']} (Score: {item['score']})")