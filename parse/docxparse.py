import docx
from typing import List


def parse_docx_document(path: str) -> str:
    """
        Функция для чтения данных и .docx документа
    """
    doc = docx.Document(path)
    text_from_doc = ""
    for text in doc.paragraphs:
        text_from_doc += text.text
        
    return text_from_doc 


def text_separator(text: str) -> List[str]:
    """
        Функция для разделения текста на более мелкие части(список строк)
    """
    separated_text = text.split("\n")
    return separated_text