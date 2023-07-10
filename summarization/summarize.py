from transformers import AutoTokenizer, T5ForConditionalGeneration
from util import MODEL_NAME, MAX_SIZE

# TODO: make spacy tokenization

def summarize(text: str) -> str:
    """
        Функция для обобщения текста на русском языке
    """
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
    input_ids = tokenizer(
        text,
        max_length=MAX_SIZE,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4, 
        max_new_tokens=None
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary