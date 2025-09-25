import os
import docx
from pdfminer.high_level import extract_text as extract_pdf_text
import re

def extract_text_from_txt(file_path):
    """
    Extracts text from a .txt file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading TXT file: {e}"

def extract_text_from_docx(file_path):
    """
    Extracts text from a .docx file.
    """
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error reading DOCX file: {e}"

def extract_text_from_pdf(file_path):
    """
    Extracts text from a .pdf file using pdfminer.six.
    """
    try:
        # pdfminer.six can extract text directly from the file path
        text = extract_pdf_text(file_path)
        # Clean up extra spaces, newlines, and form-feed characters
        return re.sub(r'[\s\n\f]+', ' ', text).strip()
    except Exception as e:
        return f"Error reading PDF file: {e}"

def extract_text(file_path):
    """
    A dispatcher function that determines the file type and calls the appropriate handler.
    """
    if not os.path.exists(file_path):
        return "Error: File not found."
    
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.txt':
        return extract_text_from_txt(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    elif file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        return "Unsupported file type"
