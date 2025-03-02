# **Die Darstellung indigener Bewohner Sibiriens**  

## 📖 **Projektbeschreibung**  
Dieses Repository enthält die Daten, Analysen und Skripte zu einer computergestützten Untersuchung der Darstellung ethnischer Gruppen in Reiseberichten des 19. und frühen 20. Jahrhunderts. Die Arbeit basiert auf den Werken von **George Kennan** und **Charles Henry Hawes** und kombiniert **manuelle Annotation, POS-Tagging und Netzwerkanalyse**, um koloniale Narrative in historischen Texten zu analysieren.  

## 📂 **Inhalt des Repositories**  
### 1️⃣ **Texte & Annotationen**    
  - `txt-Dateien/` – Enthält die **txt-Dateien** der analysierten Bücher.
  - `Catma-Exports/` – Enthält die **zip-Datein** die aus Catma exportiert wurden.
### 2️⃣ **Skripte** 
  - `Python-Skripte/'- Enthält die für die Analyse und das POS-Tagging der Adjektive notwendigen Python-Skripte
### 3️⃣ **Ergebnisse & Visualisierungen**   
  - `Netzwerkanalyse/`- Enthält die Visulisierten Ergebnisse der Netzwerkanalyse und Tabellen in zwei word-Dateien mit den gesuchten Begriffen und den häufigsten Adjektive, sowie deren Anzahl
 
## 🚀 **Installation & Nutzung**  
### 🔧 **1. Voraussetzungen**  
Bevor du die Skripte ausführst, stelle sicher, dass du folgende Pakete installiert hast:  

```bash

spaCy:
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy

de_core_news_sm:
python3 -m spacy download de_core_news_sm

📊 Datenquellen

    Bücher wurden von Project Gutenberg und Internet Archive heruntergeladen.
    Annotationen wurden mit Catma durchgeführt.
    POS-Tagging & Datenanalyse mit Python & SpaCy.

📝 Lizenz

SpaCy steht unter MIT-Lizenz. Die verwendeten Originaltexte sind gemeinfrei.

[Ronja Denneler]
📧 [st167870@stud.uni-stuttgart.de]
🔗 [RonjaDenneler]

[Yelyzaveta Honcharova]
📧 [lizagoncharova2000g@gmail.com]
🔗 [Liza24-coder]
