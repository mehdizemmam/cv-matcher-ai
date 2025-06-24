# parser/extract_cv.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"❌ Erreur lors de l'extraction du PDF : {e}")
    return text.strip()
