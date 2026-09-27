import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker_symbol, start_date, end_date):
    """
    Κατεβάζει ιστορικά δεδομένα τιμών μετοχής από το Yahoo Finance.
    """
    print(f"Fetching data for {ticker_symbol} from {start_date} to {end_date}...")
    
    # Κατέβασμα δεδομένων
    stock = yf.Ticker(ticker_symbol)
    df = stock.history(start=start_date, end=end_date)
    
    # Έλεγχος αν κατέβηκαν δεδομένα
    if df.empty:
        print("❌ No data found. Check ticker symbol or date range.")
        return None
    
    print(f"✅ Successfully downloaded {len(df)} rows of data!")
    return df

if __name__ == "__main__":
    # Παράδειγμα: Κατεβάζουμε δεδομένα για τη μετοχή της Apple (AAPL)
    ticker = "AAPL"
    start = "2023-01-01"
    end = "2024-01-01"
    
    data = fetch_stock_data(ticker, start, end)
    
    if data is not None:
        # Εμφάνιση των πρώτων 5 γραμμών του πίνακα
        print("\nFirst 5 rows of data:")
        print(data[['Open', 'High', 'Low', 'Close', 'Volume']].head())