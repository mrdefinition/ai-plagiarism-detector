import os
import pytest
from app.file_handlers import extract_text_from_txt, extract_text_from_docx, extract_text_from_pdf
from docx import Document
from reportlab.pdfgen import canvas

SAMPLES_DIR = "data/samples"

@pytest.fixture(scope="module", autouse=True)
def setup_sample_files():
    os.makedirs(SAMPLES_DIR, exist_ok=True)

    # TXT
    with open(os.path.join(SAMPLES_DIR, "sample.txt"), "w", encoding="utf-8") as f:
        f.write("This is a sample TXT file.")

    # DOCX
    doc = Document()
    doc.add_paragraph("This is a sample DOCX file.")
    doc.save(os.path.join(SAMPLES_DIR, "sample.docx"))

    # PDF
    pdf_path = os.path.join(SAMPLES_DIR, "sample.pdf")
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "This is a sample PDF file.")
    c.save()

def test_extract_text_from_txt():
    text = extract_text_from_txt(os.path.join(SAMPLES_DIR, "sample.txt"))
    assert "sample TXT" in text

def test_extract_text_from_docx():
    text = extract_text_from_docx(os.path.join(SAMPLES_DIR, "sample.docx"))
    assert "sample DOCX" in text

def test_extract_text_from_pdf():
    text = extract_text_from_pdf(os.path.join(SAMPLES_DIR, "sample.pdf"))
    assert "sample PDF" in text
