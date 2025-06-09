import os
import csv

# Folder where your CSV files are saved
csv_folder = 'scraped_reviews'

# Count reviews (rows) in each CSV
for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
        filepath = os.path.join(csv_folder, filename)
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            row_count = sum(1 for row in reader)

        print(f"{filename} → {row_count} reviews")
