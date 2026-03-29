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

def chunk_pages(pages, chunk_size=500, overlap=50):
    chunks = []
    
    for page in pages:
        words = page["text"].split()
        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i : i + chunk_size]
            chunk_text = " ".join(chunk_words)
            if len(chunk_text) < 50:
                continue
            chunks.append({
                "text": chunk_text,
                "source": page["source"],
                "page_number": page["page_number"],
                "chunk_index": len(chunks),
            })
    
    return chunks