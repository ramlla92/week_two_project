from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "bank_reviews"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as conn:
            print("✅ PostgreSQL connection successful!")
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
