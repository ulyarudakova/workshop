import collections
import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
characters = collections.defaultdict(list)
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for i in action['says']:
                characters[action['character']].append(i)

with open('characters.json','w') as w:
    json.dump(characters, w, ensure_ascii=False, indent=4)