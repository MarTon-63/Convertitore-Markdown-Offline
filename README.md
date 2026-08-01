# Markdown Converter Offline 🔄

Un'applicazione web leggera, moderna e locale per convertire file (Word, Excel, PDF, PowerPoint, ecc.) e testo in Markdown, con un'architettura ibrida ottimizzata.

Essendo pensata per la privacy e la sicurezza, l'applicazione funziona **100% offline**: nessun file o testo viene mai inviato a server esterni o API cloud.

## Funzionalità principali

* **Area Upload (Powered by MarkItDown)**: carica i tuoi documenti (.docx, .xlsx, .pptx, .pdf, ecc.) per una rapida conversione in Markdown. Ideale per i file pesanti e complessi.
* **Area Copia/incolla (powered by Quill & Markdownify)**: un editor Rich Text per incollare al volo frammenti dal web mantenendo la formattazione visiva (grassetti, elenchi). Il testo viene convertito istantaneamente e in modo chirurgico.
* **Anteprima in tempo reale**: visualizza il risultato renderizzato.
* **Azioni Rapide**: copia negli appunti con un clic o scarica il file `.md`.
* **Visualizza il codice Markdown grezzo**: visualizza il Markdown grezzo e copia il testo anche da qui per incollarlo direttamente dove vuoi. 

## Come avviare l'applicazione

Sono stati predisposti degli script automatici che gestiscono l'intero processo di setup senza bisogno di inserire comandi manuali. 
Alla prima esecuzione, il sistema creerà automaticamente un ambiente virtuale isolato (`venv`) e installerà le librerie necessarie (richiede una connessione internet solo la primissima volta). 
Il tuo browser si aprirà in automatico (di default all'indirizzo `http://localhost:8501`). Le volte successive l'avvio sarà quasi istantaneo e 100% offline.

### Per utenti Windows

1. Assicurati di avere **Python** installato sul tuo computer.
2. Fai doppio clic sul file `run.bat` presente in questa cartella.

### Per utenti macOS

1. Assicurati di avere **Python 3** installato sul tuo Mac.
2. Apri il Terminale, scrivi `chmod +x`  (con lo spazio finale), trascina il file `run_mac.command` nel Terminale e premi Invio. (Questo serve solo la prima volta per dare i permessi di esecuzione).
3. Da questo momento in poi, ti basterà fare doppio clic sul file `run_mac.command` per avviare l'app.

## Crediti e Autore

Questa applicazione è stata sviluppata e ottimizzata da **Marco Tonini**.

L'ispirazione per il progetto e l'idea originaria dell'utilizzo del tool Microsoft derivano da uno spunto dell'**Ing. Antonio Guadagno**.

## Note legali e Condizioni d'uso (Disclaimer)

Questa applicazione viene fornita in modo del tutto **gratuito** alla community.

1. **Open Source e modifiche:** sei libero di utilizzare, ispezionare, modificare e perfezionare il codice sorgente di questa applicazione secondo le tue necessità, a patto di citare l'autore, come da Licenza **Creative Commons Attribution 4.0 International (CC BY 4.0)**
2. **Esclusione di responsabilità:** il software è fornito "così com'è" (As Is), senza garanzie di alcun tipo. L'autore (Marco Tonini) declina ogni responsabilità per eventuali malfunzionamenti, perdita di dati, uso improprio o danni arrecati al computer dell'utente derivanti dall'utilizzo di questo script. Usalo a tua discrezione.
