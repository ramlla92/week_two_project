# scripts/theme_extraction.py

import pandas as pd
import os
import spacy

# Paths
INPUT_PATH = "data/processed/task2/sentiment_reviews.csv"
OUTPUT_PATH = "data/processed/task2/reviews_with_themes.csv"

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Defining example theme keywords 
THEME_KEYWORDS = {
    "Account Access Issues": ["login", "password", "account", "authentication", "access"],
    "Transaction Performance": ["transfer", "payment", "slow", "delay", "transaction", "processing"],
    "User Interface & Experience": ["ui", "interface", "design", "experience", "navigation", "layout"],
    "Customer Support": ["support", "help", "service", "response", "complaint", "chatbot"],
    "Feature Requests": ["feature", "request", "add", "improve", "functionality"]
}

def assign_theme(text):
    """Assign one or more themes to a review based on keyword matches"""
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha]
    matched_themes = set()
    for theme, keywords in THEME_KEYWORDS.items():
        if any(word in tokens for word in keywords):
            matched_themes.add(theme)
    return ", ".join(matched_themes) if matched_themes else "Other"

def main():
    # Load sentiment-annotated reviews
    df = pd.read_csv(INPUT_PATH)

    # Assign themes
    df['identified_themes'] = df['review_text'].apply(lambda x: assign_theme(str(x)))

    # Save results
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Theme extraction completed. Results saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
