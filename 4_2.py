import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open("существительные.txt", "w", encoding="utf-8") as f:
    for tokens in root.iter("tokens"):
        for token in tokens.findall("token"):
            noun = []
            for g in token.iter('g'):
                noun.append(g.attrib['v'])
            if 'NOUN' in noun and 'plur' in noun:
                f.write(token.attrib['text']+"\n")