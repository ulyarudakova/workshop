import json

with open('C:\питон\RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
roles = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = []
        for action in scene["action"]:
            characters.append(action["character"])
        roles.append(list(set(characters)))

with open('roles.json', 'w') as file:
    for line in roles:
        file.write(json.dumps(line, separators=(',', ':')))
        file.write("\n")