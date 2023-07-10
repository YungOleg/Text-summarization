import os
import docx2txt
from typing import List, Dict
from util import BASE_PATH_TO_DOCX_DIRECTORY, PREFIX

# ? Список id для теста скрипта:
ID_LIST = ["0816500000623013247", "0373100024323000018", "0372500001823000016"]


def read_docx_file(file_path: str) -> str:
    text_from_docx = docx2txt.process(file_path)
    return text_from_docx


def path_to_files(id: str) -> Dict[str, str]:
    """
        Функция для получения путей до файлов .docx
    """
    path_to_directory = new_path_to_directory(id)
    list_of_file_names = os.listdir(path_to_directory)
    list_of_paths = [path_to_directory + PREFIX + name for name in list_of_file_names]
    
    dict_of_paths = dict()
    for name in list_of_file_names:
        dict_of_paths |= {name : path_to_directory + PREFIX + name}
    # !return list_of_paths
    return dict_of_paths
    
    
def new_path_to_directory(id: str) -> str:
    """
        В корневой директории "eis" хранятся папки, названием каждой папки является id(с сайта ЕИС)
    """
    new_path = BASE_PATH_TO_DOCX_DIRECTORY + PREFIX + id
    return new_path


def get_texts_from_file() -> Dict[str, str]:
    # ! text = [read_docx_file(path) for path in path_to_files(ID_LIST[0])]
    # ! return text
    texts = dict()
    paths_dict = path_to_files(ID_LIST[0])
    for path in paths_dict.keys():
        # ! texts |= {paths_dict[path]: read_docx_file(paths_dict[path])}
        texts |= {path: read_docx_file(paths_dict[path])}
        
    return texts