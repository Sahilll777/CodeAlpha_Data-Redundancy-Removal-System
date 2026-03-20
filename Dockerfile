FROM python:3.10

WORKDIR /app

COPY ./backend /app

ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x wait-for-db.sh

CMD ["sh", "wait-for-db.sh", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]