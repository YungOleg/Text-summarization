from summarization.summarize import summarize
import time


def main():
    start = time.time()
    with open('texts/test_text.txt', encoding='utf-8') as file:
        text = file.readlines()
        print('Text is read')
        print(f"Read time: {time.time() - start}")
        
    with open('texts/finaltext.txt', 'w', encoding='utf-8') as file:
        file.write(summarize(text))
        print("Text is write")
        print(f"Write time: {time.time() - start}")


if __name__ == "__main__":
    main()
    # ! "pip freeze > requirements.txt"