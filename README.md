# Customer Experience Analytics for Fintech Apps

This project analyzes Google Play Store reviews for fintech applications to understand customer satisfaction, sentiment trends, and key issues. Insights from this analysis can guide banks in improving app performance, UI/UX, and customer support.  

---

## Structure
This repository follows a clean, data-engineering-friendly project layout:  
- **src/** – Python modules and configuration files  
- **notebooks/** – Exploratory data analysis and visualization  
- **scripts/** – Automation scripts for scraping and preprocessing  
- **data/raw/** – Raw CSVs collected from the scraper  
- **data/processed/** – Cleaned datasets ready for analysis  
- **GitHub Actions CI pipeline** – Optional for automated workflow  

---

## Task 1 – Google Play Store Review Scraping

### Objective
Collect and preprocess user reviews from the Google Play Store for three Ethiopian banks’ mobile apps:  

| Bank | App ID |
|------|--------|
| Commercial Bank of Ethiopia (CBE) | com.combanketh.mobilebanking |
| Bank of Abyssinia | com.boa.boaMobileBanking |
| Dashen Bank | com.dashen.dashensuperapp |

**Target:** Minimum of 400 reviews per bank (1,200+ total).  

### Tools and Libraries
- **Python 3.x** – main programming language  
- **google-play-scraper** – fetch app info and reviews  
- **pandas** – data cleaning and CSV export  
- **tqdm** – progress bars during scraping  
- **datetime** – review date handling  

### Project Structure Relevant to Task 1
├── src/config.py # App IDs, bank names, scraper settings, file paths
├── scripts/scrape_reviews.py # Scraper implementation
├── scripts/preprocess_reviews.py # Data preprocessing
├── data/raw/ # Raw CSVs from scraper
├── data/processed/ # Cleaned CSVs ready for analysis

### Scraping Process
1. Load configuration from `src/config.py`  
2. Fetch app metadata (ratings, total reviews, installs) → saved in `data/raw/app_info.csv`  
3. Scrape reviews using `google-play-scraper`:
   - Review text, rating, date, bank name, source  
   - Ensure minimum 400 reviews per bank  
   - Save raw data as `data/raw/reviews.csv`  

### Preprocessing Steps
- Remove duplicates using `review_id`  
- Fill missing values:  
  - Empty review text → `''`  
  - Missing ratings → `0`  
  - Missing review dates → today’s date  
- Normalize dates to `YYYY-MM-DD`  
- Keep essential columns: `review_text, rating, review_date, bank_name, source`  
- Save cleaned dataset to `data/processed/clean_reviews.csv`  

---

## Usage
1. Clone this repository:
```bash
git clone <repo-url>
cd <repo-folder>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure `src/config.py` with your app IDs and desired file paths.

4. Run the scraper:
```bash
python scripts/scrape_reviews.py
```

5. Preprocess the reviews:
```bash
python scripts/preprocess_reviews.py
```

6. Cleaned reviews will be available in `data/processed/clean_reviews.csv` for analysis or visualization.
