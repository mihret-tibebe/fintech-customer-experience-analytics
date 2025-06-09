from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
# import schedule
import logging
import time
import os

# Set up logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Bank names and their corresponding Google Play Store app IDs
BANK_APPS = {
    'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
    'Bank of Abyssinia': 'com.boa.boaMobileBanking',
    'Dashen Bank': 'com.dashen.dashensuperapp'
}

# Directory to save CSVs
OUTPUT_DIR = "scraped_reviews"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def scrape_reviews_for_bank(app_id, bank_name):
    logging.info(f"🔄 Fetching reviews for {bank_name}...")
    try:
        results, _ = reviews(
            app_id,
            lang='en',
            # country='us',
            sort=Sort.NEWEST,
            count=5000,
            filter_score_with=None
        )

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(OUTPUT_DIR, f"{bank_name.replace(' ', '_')}_reviews_{timestamp}.csv")

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
            writer.writeheader()

            for entry in results:
                writer.writerow({
                    'review_text': entry['content'],
                    'rating': entry['score'],
                    'date': entry['at'].strftime('%Y-%m-%d'),
                    'bank_name': bank_name,
                    'source': 'Google Play'
                })

        logging.info(f"✅ {len(results)} reviews saved for {bank_name} to {filename}")

    except Exception as e:
        logging.error(f"❌ Error scraping {bank_name}: {e}")

def scrape_all_banks():
    for bank_name, app_id in BANK_APPS.items():
        scrape_reviews_for_bank(app_id, bank_name)

# Scheduling options
# schedule.every().day.at("01:00").do(scrape_all_banks)
# Uncomment other options if preferred:
# schedule.every(6).hours.do(scrape_all_banks)
# schedule.every().monday.at("08:00").do(scrape_all_banks)

if __name__ == "__main__":
    logging.info("🚀 Starting one-time scrape for all banks.")
    scrape_all_banks()