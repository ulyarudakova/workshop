import csv
from collections import OrderedDict

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    price = {}
    for row in reader:
        price[row['Title']] = float(row["Price"])

dictionary = OrderedDict(sorted(price.items(), key=lambda t: t[1]))
dictionary1 = OrderedDict(sorted(price.items(), key=lambda t: t[1], reverse=True))


with open('min_price.csv', "w", encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator="\r")
    for item in dictionary:
        writer.writerow([item, dictionary[item]])
with open('max_price.csv', 'w', encoding='utf-8') as d:
    writer = csv.writer(d, lineterminator="\r")
    for item in dictionary1:
        writer.writerow([item, dictionary1[item]])