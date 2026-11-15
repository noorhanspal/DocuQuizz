import pymupdf
from docx import Document


def extract_pdf_text(file_path):
    text = ""

    with pymupdf.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()

    return text


def extract_docx_text(file_path):
    text = ""

    document = Document(file_path)

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text