# File upload extractors (PDF, DOCX, TXT)
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def extract_text_from_pdf(file_path_or_buffer):
    """
    Extract text from a PDF file.
    
    Args:
        file_path_or_buffer (str or file-like): PDF file path or uploaded file buffer
    
    Returns:
        str: Extracted text
    """
    try:
        text = extract_pdf_text(file_path_or_buffer)
        return text.strip()
    except Exception as e:
        return f"❌ Error reading PDF: {e}"

def extract_text_from_docx(file_path_or_buffer):
    """
    Extract text from a DOCX file.
    
    Args:
        file_path_or_buffer (str or file-like): DOCX file path or uploaded file buffer
    
    Returns:
        str: Extracted text
    """
    try:
        doc = Document(file_path_or_buffer)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"❌ Error reading DOCX: {e}"

def extract_text_from_txt(file_path_or_buffer):
    """
    Extract text from a plain TXT file.
    
    Args:
        file_path_or_buffer (str or file-like): TXT file path or uploaded file buffer
    
    Returns:
        str: Extracted text
    """
    try:
        if hasattr(file_path_or_buffer, "read"):  # file-like (uploaded)
            content = file_path_or_buffer.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8", errors="ignore")
        else:  # path
            with open(file_path_or_buffer, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        return content.strip()
    except Exception as e:
        return f"❌ Error reading TXT: {e}"
