from src.ingestion.pdf_loader import extract_text_from_pdf, chunk_pages

pages = extract_text_from_pdf("Getting Started with OneDrive.pdf")
chunks = chunk_pages(pages)

print(f"Total chunks: {len(chunks)}")
print(chunks[0])