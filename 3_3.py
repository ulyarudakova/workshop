import json

with open('C:\питон\RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
characters = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters[action["character"]] = 1
            else:
                characters[action["character"]] += 1

max = 0
for character in characters:
    if characters[character] >= max:
        max = characters[character]
        name = character
print(name)