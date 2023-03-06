import csv

with open('task_3.csv', 'w', encoding='utf-8') as file:
    with open('stage3_test.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(file, fieldnames=["Id", "Title", "Price"], lineterminator="\r")
        writer.writeheader()
        for row in reader:
            dot = (row["Id"], row["Title"], row["Price"])
            writer.writerow({"Id": row["Id"], "Title": row["Title"], "Price": row["Price"]})