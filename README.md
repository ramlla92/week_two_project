# Customer Experience Analytics for Fintech Apps

This project analyzes Google Play Store reviews for fintech applications to understand customer satisfaction, sentiment trends, and key issues.

## Structure
This repository follows a clean data-engineering-friendly project layout including:
- src/ for Python modules  
- notebooks/ for exploratory work  
- scripts/ for automation   
- GitHub Actions CI pipeline  

## Task 1 – Google Play Store Review Scraping

### Objective
Collect and preprocess user reviews from the Google Play Store for three Ethiopian banks’ mobile apps:

- **Commercial Bank of Ethiopia (CBE)** → `com.combanketh.mobilebanking`  
- **Bank of Abyssinia** → `com.boa.boaMobileBanking`  
- **Dashen Bank** → `com.dashen.dashensuperapp`  

**Target:** Minimum of 400 reviews per bank (1,200+ total).  

### Tools and Libraries
- **Python 3.x** – main programming language  
- **google-play-scraper** – to fetch app info and reviews  
- **pandas** – for data storage, cleaning, and CSV export  
- **tqdm** – progress bars during scraping  
- **datetime** – handling review dates  

### Project Structure Relevant to Task 1

├── src/config.py # App IDs, bank names, scraper settings, file paths

├── scripts/scrape_reviews.py # Scraper

├── scripts/preprocess_reviews.py # Preprocessing script

├── data/raw/ # Raw CSVs from scraper

├── data/processed/ # Clean CSVs ready for analysis


### Scraping Process
1. Load configuration from `src/config.py`  
2. Fetch app metadata (ratings, total reviews, installs) → saved in `data/raw/app_info.csv`  
3. Scrape reviews using `google-play-scraper`:
   - Review text, rating, date, bank name, source  
   - Minimum 400 reviews per bank  
   - Saved as `data/raw/reviews.csv`  

### Preprocessing Steps
- Remove duplicates based on `review_id`  
- Fill missing values:
  - Empty review text → `''`  
  - Missing ratings → `0`  
  - Missing review dates → today’s date  
- Normalize dates to `YYYY-MM-DD`  
- Keep essential columns: `review_text, rating, review_date, bank_name, source`  
- Save cleaned dataset to `data/processed/clean_reviews.csv`  


