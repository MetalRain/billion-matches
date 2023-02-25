FROM python:3.11.2-slim-buster as main

WORKDIR /app/

COPY main.py ./main.py
RUN ["pip", "install", "tqdm"]
CMD ["python", "main.py", "./data/labels.csv", "./data/items.csv", "./data/subscribers.csv"] 