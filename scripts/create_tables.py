from sqlalchemy import text
from db_connection import engine

create_tables_sql = """
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) UNIQUE NOT NULL,
    app_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    review_text TEXT,
    rating INTEGER,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    source VARCHAR(50)
);
"""

def main():
    with engine.connect() as conn:
        conn.execute(text(create_tables_sql))
        conn.commit()
        print("✅ Tables created successfully!")

if __name__ == "__main__":
    main()
