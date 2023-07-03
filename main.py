from summarize import summarize
import time


def main():
    start = time.time()
    with open('test_text.txt', encoding='utf-8') as file:
        text = file.readlines()
        print('Text is read')
        print(f"Read time: {time.time() - start}")
        
    with open('finaltext.txt', encoding='utf-8') as file:
        print(summarize(text), file=file)
        print("Text is write")
        print(f"Write time: {time.time() - start}")


if __name__ == "__main__":
    main()
    # pip install transformers==4.30.2
    # ? pip install docx-parser==1.0.1
    # ? pip install sentencepiece==0.1.99
    # ? pip install torch