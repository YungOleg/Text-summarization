FROM python

WORKDIR /app

COPY . .

RUN python -m venv .venv

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]