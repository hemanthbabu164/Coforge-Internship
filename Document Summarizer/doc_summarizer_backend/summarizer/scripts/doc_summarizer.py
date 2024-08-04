import spacy
from PyPDF2 import PdfReader
import docx
from transformers import pipeline
import json

# Load NLP models
nlp = spacy.load('en_core_web_sm')
summarizer = pipeline('summarization')

def read_document(file_path):
    try:
        if file_path.endswith('.pdf'):
            return read_pdf(file_path)
        elif file_path.endswith('.docx'):
            return read_docx(file_path)
        elif file_path.endswith('.txt'):
            return read_txt(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Error reading document: {e}")
        return ""

def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        return content
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        content = "\n".join([para.text for para in doc.paragraphs])
        return content
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

def read_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading TXT: {e}")
        return ""

# Other functions remain the same

# Main function
def main(file_path, output_path):
    content = read_document(file_path)
    if not content:
        print("No content to process.")
        return
    key_value_pairs = preprocess_document(content)
    save_key_value_pairs(key_value_pairs, output_path)
    return key_value_pairs
