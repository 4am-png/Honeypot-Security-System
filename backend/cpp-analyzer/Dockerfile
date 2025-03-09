FROM gcc:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y cmake

RUN cmake . && make

CMD ["./honeypot_analyzer"]
