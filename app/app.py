import sys, os
# Add the project root (A.I.P) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
def test_placeholder():
    import streamlit as st
import tempfile
import os
from app.file_handlers import extract_text
from app.analysis import analyze_text

st.title("AI Plagiarism Detector 📘")

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

if uploaded_file is not None:
    # Use a temporary file to handle the upload securely
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        file_path = temp_file.name

    # Extract + analyze
    st.subheader("Extracted Text:")
    try:
        text = extract_text(file_path)
        if "Error" in text:
            st.error(text)
        else:
            st.write(text[:500] + "..." if len(text) > 500 else text)
            
            # Analyze the text
            result = analyze_text(text)
            st.subheader("Detection Result:")
            st.json(result)

    finally:
        # Ensure the temporary file is deleted after use
        os.remove(file_path)
