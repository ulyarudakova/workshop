import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    with open('task_1.csv', 'w', encoding='utf-8') as file:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames, lineterminator="\r")
        for row in reader:
            rows = row['Images']
            if len(rows.split(',')) > 3:
                writer.writerow(row)
