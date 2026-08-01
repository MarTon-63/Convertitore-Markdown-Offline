# MARKDOWN CONVERTER OFFLINE 🔄

Un'applicazione web leggera, moderna e locale per convertire file (Word, Excel, PDF, PowerPoint, ecc.) e testo in Markdown, con un'architettura ibrida ottimizzata.

Essendo pensata per la privacy e la sicurezza, l'applicazione funziona **100% offline**: nessun file o testo viene mai inviato a server esterni o API cloud.

## Funzionalità principali

* **Area Upload (powered by MarkItDown)**: carica i tuoi documenti (.docx, .xlsx, .pptx, .pdf, ecc.) per una rapida conversione in Markdown. Ideale per i file pesanti e complessi.
* **Area Copia/incolla (powered by Quill & Markdownify)**: un editor Rich Text per incollare - e modificare - al volo frammenti dal web mantenendo la formattazione visiva (grassetti, elenchi). Il testo viene convertito istantaneamente e in modo chirurgico.
* **Anteprima in tempo reale**: visualizza il risultato renderizzato.
* **Azioni Rapide**: copia negli appunti con un clic o scarica il file `.md`.
* **Visualizza il codice Markdown grezzo**: visualizza il Markdown grezzo, e ti permette di copiarlo manualmente e di incollarlo direttamente dove vuoi. 

## Come avviare l'applicazione

Sono stati predisposti degli script automatici che gestiscono l'intero processo di setup senza bisogno di inserire comandi manuali. 
Alla prima esecuzione, il sistema creerà automaticamente un ambiente virtuale isolato (`venv`) e installerà le librerie necessarie (richiede una connessione internet solo la primissima volta). 
Il tuo browser si aprirà in automatico (di default all'indirizzo `http://localhost:8501`). Le volte successive l'avvio sarà quasi istantaneo e 100% offline.

### Passaggi preliminari (per tutti gli utenti)

1. Scarica questa applicazione cliccando sul pulsante verde **"<> Code"** in alto in questa pagina e selezionando **"Download ZIP"**.
2. Estrai il file ZIP appena scaricato in una posizione a tua scelta sul tuo computer (ad esempio, sul Desktop).
3. Apri la cartella appena estratta (probabilmente si chiamerà `Convertitore-Markdown-Offline-main`).

### Per utenti Windows

1. Assicurati di avere **Python** installato sul tuo computer.
2. All'interno della cartella appena estratta, fai doppio clic sul file `run.bat`.
3. Si aprirà il Terminale, che scaricherà le librerie necessarie e creerà in automatico l'ambiente isolato (la cartella `venv`). Questa operazione può richiedere qualche minuto, ma avviene solo la primissima volta.
4. Al termine del processo, l'applicazione si aprirà da sola nel tuo browser. (Se il Terminale dovesse mettersi in pausa, premi semplicemente Invio).

### Per utenti macOS

1. Assicurati di avere Python 3 installato sul tuo Mac.
2. All'interno della cartella appena estratta, individua il file `run_mac.command`.
3. Apri il Terminale, scrivi `chmod +x ` (con lo spazio finale), trascina il file `run_mac.command` nel Terminale e premi Invio. Questo serve solo la prima volta per dare i permessi di esecuzione. (Una volta premuto Invio, puoi tranquillamente chiudere questa finestra del Terminale).
4. Torna nella tua cartella e fai doppio clic sul file `run_mac.command`. Il Mac aprirà automaticamente una nuova finestra del Terminale: attendi che il sistema scarichi le librerie necessarie e crei in automatico l'ambiente isolato (la cartella `venv`). Questa operazione può richiedere qualche minuto, ma avviene solo la primissima volta.
5. Al termine del processo, l'applicazione si aprirà da sola nel tuo browser. Da questo momento in poi, le volte successive ti basterà fare doppio clic sul file `run_mac.command` e l'avvio sarà quasi istantaneo.

## Crediti e Autore

Questa applicazione è stata sviluppata e ottimizzata da **Marco Tonini**.

L'ispirazione per il progetto e l'idea originaria dell'utilizzo del tool Microsoft derivano da uno spunto dell'**Ing. Antonio Guadagno**.

## Note legali e Condizioni d'uso (Disclaimer)

Questa applicazione viene fornita in modo del tutto **gratuito** alla community.

1. **Open Source e modifiche**: sei libero di utilizzare, ispezionare, modificare e perfezionare il codice sorgente di questa applicazione secondo le tue necessità, a patto di citare l'autore, come da Licenza **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
2. **Uso non commerciale**: è severamente vietato utilizzare questa applicazione, o parti del suo codice, per scopi commerciali, rivenderla, monetizzarla o inserirla in prodotti a pagamento.
3. **Esclusione di responsabilità**: il software è fornito "così com'è" (As Is), senza garanzie di alcun tipo. L'autore (Marco Tonini) declina ogni responsabilità per eventuali malfunzionamenti, perdita di dati, uso improprio o danni arrecati al computer dell'utente derivanti dall'utilizzo di questo script. Usalo a tua discrezione.
