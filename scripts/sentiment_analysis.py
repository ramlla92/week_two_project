# scripts/sentiment_analysis.py

import pandas as pd
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Paths
RAW_DATA_PATH = "data/processed/clean_reviews.csv"
OUTPUT_PATH = "data/processed/task2/sentiment_reviews.csv"

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def main():
    # Load cleaned reviews
    df = pd.read_csv(RAW_DATA_PATH)

    # Initialize VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Apply sentiment analysis
    df['sentiment_score'] = df['review_text'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'POSITIVE' if x > 0.05 else 'NEGATIVE' if x < -0.05 else 'NEUTRAL'
    )

    # Save results
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Sentiment analysis completed. Results saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
