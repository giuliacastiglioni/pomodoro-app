"""
Streamlit passa il contenuto di st.markdown(..., unsafe_allow_html=True)
attraverso un parser Markdown prima di iniettarlo come HTML. Se una stringa
multi-riga contiene righe indentate (4+ spazi, tipico di codice Python
formattato), il parser le interpreta come un blocco di codice e le mostra
come testo grezzo invece di renderizzarle come SVG/HTML.

Questa utility appiattisce l'SVG/HTML su un'unica riga (senza newline né
indentazione) per evitare il problema, mantenendo il markup valido: SVG e
HTML non sono sensibili agli spazi bianchi tra i tag.
"""


def flatten_html(markup):
    lines = [line.strip() for line in markup.strip().splitlines()]
    return " ".join(line for line in lines if line)
