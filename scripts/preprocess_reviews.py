"""
Preprocess Google Play Store reviews
- Remove duplicates
- Handle missing values
- Normalize dates
- Save clean CSV
"""

import sys
import os
import pandas as pd
from datetime import datetime
from src.config import DATA_PATHS

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def preprocess_reviews():
    """Load raw reviews, clean them, and save a processed CSV"""
    
    # Load raw reviews
    if not os.path.exists(DATA_PATHS['raw_reviews']):
        print(f"ERROR: Raw reviews not found at {DATA_PATHS['raw_reviews']}")
        return
    
    df = pd.read_csv(DATA_PATHS['raw_reviews'])
    print(f"Loaded {len(df)} raw reviews")

    # --- Step 1: Remove duplicates ---
    before = len(df)
    df.drop_duplicates(subset=['review_id'], inplace=True)
    after = len(df)
    print(f"Removed {before - after} duplicate reviews")

    # --- Step 2: Handle missing values ---
    # Fill missing review text with empty string
    df['review_text'].fillna('', inplace=True)
    # Fill missing ratings with 0
    df['rating'].fillna(0, inplace=True)
    # Fill missing dates with today's date
    df['review_date'] = pd.to_datetime(df['review_date'], errors='coerce')
    df['review_date'].fillna(pd.Timestamp(datetime.today()), inplace=True)

    # --- Step 3: Normalize dates ---
    df['review_date'] = df['review_date'].dt.strftime('%Y-%m-%d')

    # --- Step 4: Select essential columns ---
    clean_df = df[['review_text', 'rating', 'review_date', 'bank_name', 'source']]
    
    # --- Step 5: Save cleaned CSV ---
    os.makedirs(DATA_PATHS['processed'], exist_ok=True)
    processed_path = os.path.join(DATA_PATHS['processed'], 'clean_reviews.csv')
    clean_df.to_csv(processed_path, index=False)
    
    print(f"Cleaned data saved to {processed_path}")
    print(f"Total reviews after cleaning: {len(clean_df)}")

    return clean_df

if __name__ == "__main__":
    preprocess_reviews()
