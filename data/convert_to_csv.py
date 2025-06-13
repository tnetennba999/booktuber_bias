import csv

# Step 1: Read the text data
with open("cleaned_output.txt", "r", encoding="utf-8") as f:
    lines = [line.strip().rstrip(';') for line in f if line.strip()]

# Step 2: Group every 6 lines into one record
book_records = [lines[i:i+6] for i in range(0, len(lines), 6)]

# Step 3: Define headers
headers = ["Title", "Author", "Average_Rating", "Booktuber_Rating", "Date_Read", "Date_Added"]

# Step 4: Write to CSV
with open("jack_edwards_goodread_cleaned.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(book_records)
