"""
Configuration file for Google Play Store Scraper
Focus: Three Ethiopian banks
"""

# Google Play app IDs for each bank
APP_IDS = {
    "CBE": "com.combanketh.mobilebanking",
    "ABYSSINIA": "com.boa.boaMobileBanking",
    "DASHEN": "com.dashen.dashensuperapp"
}

# Full bank names for labeling
BANK_NAMES = {
    "CBE": "Commercial Bank of Ethiopia",
    "ABYSSINIA": "Bank of Abyssinia",
    "DASHEN": "Dashen Bank"
}

# Scraper behavior settings
SCRAPING_CONFIG = {
    "reviews_per_bank": 400,  # Minimum 400 reviews per bank
    "lang": "en",             # Language of reviews
    "country": "us",          # Region for Google Play
    "max_retries": 5          # Retry if network fails
}

# Paths to save scraped data
DATA_PATHS = {
    "raw": "data/raw",
    "processed": "data/processed",
    "raw_reviews": "data/raw/reviews.csv",
    "app_info": "data/raw/app_info.csv"
}
