## 📌 Methodology

### 🧾 1. **Data Collection (Web Scraping)**

We used the [`google-play-scraper`](https://pypi.org/project/google-play-scraper/) Python package to collect user reviews for mobile banking apps from the Google Play Store. The goal was to collect at least **400 reviews per bank** (CBE, BOA, Dashen).

Key steps:

* Scraped up to 5,000 most recent reviews per app.
* Captured key fields: `review_text`, `rating`, `date`, `bank_name`, and `source`.
* App IDs were obtained from the official Google Play Store URLs.
* Scheduled scraping functionality was included for potential automation, though this run was manual.

Each bank’s reviews were saved into a separate CSV file with timestamped filenames in the `scraped_reviews/` directory.

---

### 🧼 2. **Data Preprocessing**

Once collected, the raw reviews were loaded and cleaned to produce a unified dataset for analysis.

Key preprocessing steps:

* **Concatenated** reviews from all banks into a single DataFrame.
* **Removed duplicates** using a combination of `review_text`, `rating`, and `bank_name` to retain only truly unique feedback per bank.
* **Dropped incomplete entries**, i.e., reviews with missing text, rating, or date.
* **Standardized date format** to `YYYY-MM-DD`.
* Selected and reordered columns to ensure consistency:
  `review_text`, `rating`, `date`, `bank_name`, `source`

The cleaned dataset was saved as `cleaned_reviews.csv`, ready for downstream sentiment and thematic analysis.

---

### ⚙️ 3. **Tools & Environment**

* Python 3.x
* Libraries: `google-play-scraper`, `pandas`, `csv`, `schedule`
* Logging with built-in `logging` module
* Code versioned via Git (`task-1` branch)

---