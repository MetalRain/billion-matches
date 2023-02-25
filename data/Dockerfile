FROM python:3.11.2-slim-buster

WORKDIR /app/

RUN ["pip", "install", "tqdm"]
COPY main.py ./main.py
CMD ["python", "main.py"]