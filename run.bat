@echo off
echo =======================================================
echo   Inizializzazione Markdown Converter Offline...
echo =======================================================

cd /d "%~dp0"

IF NOT EXIST "venv" (
    echo.
    echo Creazione dell'ambiente virtuale...
    python -m venv venv
) ELSE (
    echo.
    echo Ambiente virtuale gia' esistente.
)

echo.
echo Attivazione dell'ambiente e installazione dipendenze...
call venv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Avvio dell'applicazione web...
streamlit run app.py

pause
