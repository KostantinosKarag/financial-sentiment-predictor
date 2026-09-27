import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from fetch_data import fetch_stock_data

def prepare_data_and_train(ticker="AAPL", start="2022-01-01", end="2024-01-01"):
    # 1. Αντλούμε τα ιστορικά δεδομένα
    df = fetch_stock_data(ticker, start, end)
    if df is None or df.empty:
        return

    # 2. Υπολογισμός Τεχνικών Δεικτών (Feature Engineering)
    # Ημερήσια επιστροφή (Daily Return)
    df['Return'] = df['Close'].pct_change()
    
    # Κινητοί μέσοι όροι (Moving Averages)
    df['MA_5'] = df['Close'].rolling(window=5).mean()
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    
    # Μεταβλητότητα (Volatility)
    df['Volatility'] = df['Return'].rolling(window=5).std()

    # 3. Ορισμός του Στόχου (Target): 1 αν η μετοχή ανέβει αύριο, 0 αν πέσει
    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

    # Καθαρισμός κενών τιμών (NaN) λόγω των rolling windows
    df = df.dropna()

    # Features (Είσοδοι για το AI) και Target (Έξοδος)
    features = ['Close', 'Volume', 'Return', 'MA_5', 'MA_20', 'Volatility']
    X = df[features]
    y = df['Target']

    # 4. Διαχωρισμός σε Train και Test sets (80% Εκπαίδευση, 20% Δοκιμή)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # 5. Εκπαίδευση Μοντέλου Random Forest
    print(f"\n🤖 Training Machine Learning Model (Random Forest) for {ticker}...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 6. Αξιολόγηση Μοντέλου
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"✅ Model Training Complete!")
    print(f"📊 Accuracy Score: {accuracy * 100:.2f}%\n")
    print("Detailed Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    prepare_data_and_train()