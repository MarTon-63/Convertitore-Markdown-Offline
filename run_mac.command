#!/bin/bash

# Questo script avvia l'app Markdown Converter Offline su macOS

# Spostati nella cartella in cui si trova questo script

cd "$(dirname "$0")"

echo "Avvio Markdown Converter Offline in corso..."

# Controlla se la cartella dell'ambiente virtuale (venv) esiste già

if [ ! -d "venv" ]; then echo "Primo avvio rilevato. Creazione dell'ambiente virtuale in corso..." python3 -m venv venv

echo "Attivazione dell'ambiente virtuale..."
source venv/bin/activate

echo "Installazione delle librerie necessarie (potrebbe richiedere qualche minuto)..."
pip install -r requirements.txt

else echo "Ambiente virtuale trovato. Attivazione in corso..." source venv/bin/activate fi

# Avvia l'applicazione Streamlit

echo "Avvio di Streamlit..." streamlit run app.py