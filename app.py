import streamlit as st
import tempfile
import os
import pyperclip
from markitdown import MarkItDown
from streamlit_quill import st_quill
from markdownify import markdownify as md_convert

# Configurazione della pagina
st.set_page_config(
    page_title="Markdown Converter Offline",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Stili CSS personalizzati per un design più moderno
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextArea textarea {
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    [data-testid="stHeader"] {
        display: none;
    }
    .stDownloadButton button, .stButton button {
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔄 Markdown Converter Offline")
st.markdown("**Converti i tuoi documenti (Word, Excel, PDF, ecc.) e il tuo testo in Markdown, in modo 100% locale e sicuro.** Nessun dato viene inviato a servizi esterni.")

md = MarkItDown()

if "markdown_output" not in st.session_state:
    st.session_state.markdown_output = ""

tabs = st.tabs(["📁 Area Upload", "📝 Area Copia/Incolla"])

with tabs[0]:
    st.markdown("### Carica il file da convertire")
    uploaded_file = st.file_uploader(
        "Formati supportati: .docx, .xlsx, .pptx, .pdf, .html, .csv, .json, .txt",
        type=["docx", "xlsx", "pptx", "pdf", "html", "csv", "json", "txt"],
        label_visibility="collapsed"
    )
    if st.button("Converti File in Markdown", type="primary"):
        if uploaded_file is not None:
            with st.spinner("Elaborazione del file in corso..."):
                try:
                    # Ottieni l'estensione del file
                    ext = f".{uploaded_file.name.split('.')[-1]}" if '.' in uploaded_file.name else ""
                    
                    # Salva temporaneamente il file caricato
                    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name

                    # Converte usando MarkItDown
                    result = md.convert(tmp_file_path)
                    st.session_state.markdown_output = result.text_content
                    
                    # Rimuove il file temporaneo per sicurezza/pulizia
                    os.remove(tmp_file_path)
                    
                    st.success("Conversione completata con successo! Scorri in basso per l'anteprima.")
                except Exception as e:
                    st.error(f"Errore durante la conversione del file: {e}")
        else:
            st.warning("Seleziona un file prima di cliccare su Converti.")

with tabs[1]:
    st.markdown("### Incolla il contenuto")
    st.markdown("Incolla qui testo formattato (es. da una pagina web o Word). La formattazione verrà convertita in Markdown.")
    
    # Renderizza il Rich Text Editor che restituisce l'HTML
    text_input = st_quill(placeholder="Incolla qui il testo formattato (Ctrl+V)...", html=True)
    
    if st.button("Converti Testo in Markdown", type="primary"):
        if text_input and text_input.strip():
            with st.spinner("Elaborazione del testo in corso..."):
                try:
                    # Usa markdownify per convertire l'HTML frammentato generato da Quill
                    st.session_state.markdown_output = md_convert(text_input, heading_style="ATX")
                    
                    st.success("Conversione completata con successo! Scorri in basso per l'anteprima.")
                except Exception as e:
                    st.error(f"Errore durante la conversione: {e}")
        else:
            st.warning("Incolla del testo nell'area prima di cliccare su Converti.")

st.divider()

st.subheader("👁️ Anteprima Markdown")

if st.session_state.markdown_output:
    # Mostra l'anteprima renderizzata
    with st.container(border=True):
        st.markdown(st.session_state.markdown_output)
    
    st.divider()
    
    st.subheader("🚀 Azioni Rapide")
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="⬇️ Scarica come file .md",
            data=st.session_state.markdown_output,
            file_name="risultato.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    with col2:
        if st.button("📋 Copia negli Appunti", use_container_width=True):
            try:
                pyperclip.copy(st.session_state.markdown_output)
                st.toast("Markdown copiato negli appunti!", icon="✅")
            except Exception as e:
                st.error(f"Errore durante la copia: {e}. Il tuo sistema potrebbe non supportare questa funzione nativamente.")
    
    # Mostra anche il raw markdown code per comodità, nel caso la copia fallisca
    with st.expander("Visualizza il codice Markdown grezzo"):
        st.code(st.session_state.markdown_output, language="markdown")
else:
    st.info("Nessun contenuto da mostrare. Carica un file o incolla del testo per iniziare.")

    # --- INIZIO FOOTER CREDITI ---
st.write("") # Spazio vuoto
st.markdown("""
<div style="text-align: center; font-size: 0.75rem; color: #6c757d; line-height: 1.3; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e6e6e6;">
    <p style="margin: 0; padding: 2px 0;">© 2026 <strong>Marco Tonini</strong> | Idea originale: <strong>Ing. Antonio Guadagno</strong></p>
    <p style="margin: 0; padding: 2px 0;">Distribuito con licenza <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" style="color: #6c757d; text-decoration: underline;">Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)</a>. Sei libero di condividere e modificare l'app, a patto di citare l'autore.</p>
    <p style="margin: 0; padding: 2px 0;">⚠️ <em>Software fornito gratuitamente 'così com'è'. L'autore declina ogni responsabilità per uso improprio o eventuali danni.</em></p>
</div>
""", unsafe_allow_html=True)
# --- FINE FOOTER CREDITI ---
