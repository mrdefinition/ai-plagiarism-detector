import os
from typing import Optional

# TXT
def extract_text_from_txt(file_path: str) -> str:
    """Extract text from a plain text (.txt) file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[Error reading TXT file: {e}]"


# DOCX
def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a Word (.docx) file."""
    try:
        from docx import Document
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"[Error reading DOCX file: {e}]"


# PDF
def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    try:
        import PyPDF2
        text = []
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text.append(page.extract_text() or "")
        return "\n".join(text)
    except Exception as e:
        return f"[Error reading PDF file: {e}]"


# Dispatcher
def extract_text(file_path: str) -> Optional[str]:
    """Dispatch to correct handler based on file extension."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".txt":
        return extract_text_from_txt(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".pdf":
        return extract_text_from_pdf(file_path)
    else:
        return f"[Unsupported file type: {ext}]"
