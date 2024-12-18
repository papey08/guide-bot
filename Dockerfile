FROM python:3.12.3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_KEY=7778344289:AAEYlfp8auNpvoSAsjBdkpqG0jSTTq5c7o4

CMD ["python", "main.py"]
