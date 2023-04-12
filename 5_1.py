import collections
import json
from collections import Counter

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
words = []
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for say in action['says']:
                for line in say.split(' '):
                    words.append(line)

counts = Counter(words).most_common(20)
print(f"Самые частые:{counts}")
least_common = collections.Counter(words).most_common()[-21::]
print(f"Самые редкие: {least_common}")