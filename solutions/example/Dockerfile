FROM python:3.11.2-slim-buster as main

WORKDIR /app/

RUN ["pip", "install", "tqdm"]
COPY main.py ./main.py
CMD ["python", "main.py", "./data/labels.csv", "./data/items.csv", "./data/subscribers.csv"] 