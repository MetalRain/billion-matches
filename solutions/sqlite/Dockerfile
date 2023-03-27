FROM debian:11.6

WORKDIR /app/

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "sqlite3"]

COPY main.sql ./main.sql
CMD [ "sqlite3", "test.db", "-init", "main.sql"]