import fitz
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        if not text:
            continue
        pages.append({
            "page_number": i + 1,
            "text": text,
            "source": Path(pdf_path).name
        })

    return pages