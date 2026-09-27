import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Κατέβασμα του βασικού λεξικού VADER
nltk.download('vader_lexicon', quiet=True)

def create_financial_analyzer():
    """
    Δημιουργεί έναν Sentiment Analyzer εμπλουτισμένο με χρηματοοικονομική ορολογία.
    """
    sia = SentimentIntensityAnalyzer()
    
    # Εμπλουτισμός του λεξικού με οικονομικούς όρους (Financial Lexicon Updates)
    financial_lexicon = {
        'plummet': -3.0,
        'plummets': -3.0,
        'plummeted': -3.0,
        'surge': 3.0,
        'surges': 3.0,
        'surged': 3.0,
        'record-breaking': 2.5,
        'beating': 2.0,
        'beat': 2.0,
        'outperform': 2.5,
        'underperform': -2.5,
        'bullish': 3.0,
        'bearish': -3.0,
        'inflation': -1.5,
        'fears': -2.0,
    }
    
    sia.lexicon.update(financial_lexicon)
    return sia

def analyze_financial_sentiment(news_headlines):
    """
    Αναλύει τίτλους ειδήσεων με το προσαρμοσμένο οικονομικό λεξικό.
    """
    sia = create_financial_analyzer()
    results = []

    for headline in news_headlines:
        scores = sia.polarity_scores(headline)
        compound_score = scores['compound']
        
        if compound_score >= 0.05:
            sentiment = "POSITIVE"
        elif compound_score <= -0.05:
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"
            
        results.append({
            "headline": headline,
            "sentiment": sentiment,
            "score": round(compound_score, 4)
        })
        
    return results

if __name__ == "__main__":
    sample_news = [
        "Apple reports record-breaking quarterly revenue driven by strong iPhone sales.",
        "Tech stocks plummet as inflation fears raise interest rate concerns.",
        "Federal Reserve maintains current interest rates following monthly review.",
        "NVIDIA launches new AI chip, beating all market expectations."
    ]

    print("Analyzing news sentiment with Custom Financial VADER...\n")
    analysis = analyze_financial_sentiment(sample_news)

    for item in analysis:
        print(f"📰 Headline: {item['headline']}")
        print(f"📊 Sentiment: {item['sentiment']} (Score: {item['score']})\n")