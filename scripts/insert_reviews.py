import pandas as pd
from sqlalchemy import text
from db_connection import engine

DATA_PATH = "data/processed/task2/reviews_with_themes.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    with engine.begin() as conn:

        # ✅ Insert unique banks first
        banks = df[["bank_name"]].drop_duplicates()

        for _, row in banks.iterrows():
            conn.execute(
                text("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (:bank_name, :app_name)
                ON CONFLICT (bank_name) DO NOTHING
                """),
                {
                    "bank_name": row["bank_name"],
                    "app_name": row["bank_name"] + " Mobile App"
                }
            )

        print("✅ Banks inserted successfully!")

        # ✅ Insert reviews
        for _, row in df.iterrows():
            conn.execute(
                text("""
                INSERT INTO reviews (
                    bank_id, review_text, rating, review_date,
                    sentiment_label, sentiment_score, source
                )
                VALUES (
                    (SELECT bank_id FROM banks WHERE bank_name=:bank_name),
                    :review_text, :rating, :review_date,
                    :sentiment_label, :sentiment_score, :source
                )
                """),
                {
                    "bank_name": row["bank_name"],
                    "review_text": row["review_text"],
                    "rating": int(row["rating"]),
                    "review_date": None,
                    "sentiment_label": row["sentiment_label"],
                    "sentiment_score": float(row["sentiment_score"]),
                    "source": "Google Play"
                }
            )

        print("✅ Reviews inserted successfully!")

if __name__ == "__main__":
    main()
