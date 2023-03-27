import json

dictionary = {}
with open('C:\питон\wikidata_1000.json', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        key = data["label"]["value"]
        if "description" in line:
            value = data["description"]["value"]
        else:
            value = None
        dictionary[key] = value

with open('dictionary.json', 'w', encoding='utf-8') as file:
    json.dump(dictionary, file, ensure_ascii=False, indent=4)