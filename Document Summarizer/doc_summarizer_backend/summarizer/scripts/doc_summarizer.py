import spacy
from PyPDF2 import PdfReader
import docx
from transformers import pipeline
import json
# Load NLP models
nlp = spacy.load('en_core_web_sm')
summarizer = pipeline('summarization')

def read_document(file_path):
    if file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    elif file_path.endswith('.txt'):
        return read_txt(file_path)
    else:
        raise ValueError("Unsupported file format")

def read_pdf(file_path):
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

def read_docx(file_path):
    doc = docx.Document(file_path)
    content = "\n".join([para.text for para in doc.paragraphs])
    return content

def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def merge_short_lines(content, threshold=40):
    lines = content.split('\n')
    merged_lines = []
    current_line = ""

    for line in lines:
        if len(line.strip()) < threshold:
            current_line += " " + line.strip()
        else:
            if current_line:
                merged_lines.append(current_line.strip())
                current_line = ""
            merged_lines.append(line.strip())

    if current_line:
        merged_lines.append(current_line.strip())

    return "\n".join(merged_lines)

def preprocess_document(file_path):
    content = read_document(file_path)
    print("RRR")
    # Merge short lines into paragraphs
    content = merge_short_lines(content)
    
    # Tokenize into sentences
    doc = nlp(content)
    paragraphs = content.split("\n\n")
    sentences = [sent.text for sent in doc.sents]
    
    # Extract keywords and summarize each Paragraph
    key_value_pairs = {}
    for paragraph in paragraphs:
        keywords = extract_keywords(paragraph)
        summary = generate_summary(paragraph)
        key_value_pairs[paragraph] = {'keywords': keywords, 'summary': summary}
    
    return key_value_pairs

def extract_keywords(sentence):
    doc = nlp(sentence)
    keywords = [chunk.text for chunk in doc.noun_chunks]
    return keywords

def generate_summary(paragraph):
    # Using transformer-based summarizer
    summary = summarizer(paragraph, max_length=70, min_length=40, do_sample=False)
    return summary[0]['summary_text']


# Save key-value pairs to a JSON file
def save_key_value_pairs(key_value_pairs, output_path):
    with open(output_path, 'w') as file:
        json.dump(key_value_pairs, file, indent=4)

# Main function
def main(file_path, output_path):
    key_value_pairs = preprocess_document(file_path)
    save_key_value_pairs(key_value_pairs, output_path)
    return key_value_pairs

# Example usage
if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    file_path = r"./Testing/short.pdf"
    output_path = r"./Testing/summary_output_short.json"
    key_value_pairs = main(file_path, output_path)
    print(key_value_pairs)
