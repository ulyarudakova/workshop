import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    with open('task2.csv', 'w', encoding='utf-8') as file:
        reader = csv.reader(f)
        next(reader, None)
        writer = csv.writer(file, lineterminator="\r")
        for row in reader:
            rows = int(float(row[4]))
            if 10000 < rows < 50000:
                writer.writerow(row)