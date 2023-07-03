FROM python

WORKDIR /app

COPY . .

# RUN pip install -r dependencies.txt

CMD [ "python", "main.py" ]