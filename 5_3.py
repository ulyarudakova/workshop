import json
import collections

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
count = collections.Counter()
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                count[action['character']] += 1

print(count)