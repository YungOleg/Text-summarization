from summarization.summarize import summarize
import logging
import time
from docx_worker.docxparse import parse_docx_document

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def open_text(path: str) -> str:
    with open(path, encoding='utf-8') as file:
        text = file.read()
 
    log.info('Text is read')
    return text


def write_result(path: str, text: str):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(summarize(text))
        
    log.info("Text is write")
    
    

def main():
    start = time.time()
    
    text = open_text("texts/test.txt")
    log.info(f"Read time: {time.time() - start}")
        
    write_result("texts/result.txt", text)
    log.info(f"Write time: {time.time() - start}")

if __name__ == "__main__":
    main()
    # ! "pip freeze > requirements.txt"