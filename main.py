import time
from docx_worker import get_texts_from_file
from summarization import summarize
from logger import log

# TODO: import asyncio

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
    # start = time.time()
    
    # text = open_text("texts/test.txt")
    # log.info(f"Read time: {time.time() - start}")
        
    # write_result("texts/result.txt", text)
    # log.info(f"Write time: {time.time() - start}")
    
    # for path in path_to_files(ID_LIST[0]):
    #     print(path)
    
    
    lista = get_texts_from_file()
    for i in lista.keys():
        log.info(f"{i} : {len(lista[i])}")


if __name__ == "__main__":
    main()
    # ? "pip freeze > requirements.txt"