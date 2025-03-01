import spacy

# Laden des deutschsprachigen POS-Tagging-Modells
nlp = spacy.load("de_core_news_sm")

# Öffnen und Lesen der Textdatei
with open('C:/Users/ronja/OneDrive/Desktop/Osten.txt', 'r', encoding="UTF-8") as file:
    osten = file.read()

# POS-Tagging mit SpaCy
doc2 = nlp(osten)

# Listen für Tokens und deren POS-Tags
tokenlist = [token.text for token in doc2]
poslist = [token.pos_ for token in doc2]

# Dictionary für Adjektive
adjdic = {}

def adjsearch1(x):
    for index, word in enumerate(tokenlist):
        if word == x:
            # Verhindere Indexfehler durch Überprüfung der Grenzen
            adj_positions = []
            if index - 3 >= 0: adj_positions.append((index - 3, tokenlist[index - 3], poslist[index - 3]))
            if index - 2 >= 0: adj_positions.append((index - 2, tokenlist[index - 2], poslist[index - 2]))
            if index - 1 >= 0: adj_positions.append((index - 1, tokenlist[index - 1], poslist[index - 1]))
            if index + 1 < len(tokenlist): adj_positions.append((index + 1, tokenlist[index + 1], poslist[index + 1]))
            if index + 2 < len(tokenlist): adj_positions.append((index + 2, tokenlist[index + 2], poslist[index + 2]))
            if index + 3 < len(tokenlist): adj_positions.append((index + 3, tokenlist[index + 3], poslist[index + 3]))

            # Adjektive sammeln
            for _, adj_word, pos in adj_positions:
                if pos == "ADJ":
                    if adj_word in adjdic:
                        adjdic[adj_word] += 1
                    else:
                        adjdic[adj_word] = 1

# Testaufruf

adjsearch1("Buräten")

adjsearch1("Buräte")

adjsearch1("Burätische")

adjsearch1("Burätin")

adjsearch1("Buräten")


# Sortiere das Dictionary nach Häufigkeit (höchste zuerst)
sorted_adjdic = sorted(adjdic.items(), key=lambda item: item[1], reverse=True)

# Ausgabe der sortierten Werte
for key, value in sorted_adjdic:
    print(f"Wort: {key}, Wert: {value}")