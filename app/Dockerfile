# Dockerfile у директорії app/
FROM python:3.9-slim

WORKDIR /app

# Копіюємо requirements.txt з кореневої директорії в контейнер
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run"]
