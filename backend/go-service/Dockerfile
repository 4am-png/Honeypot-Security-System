FROM golang:1.21-alpine

WORKDIR /app

COPY . .

RUN go mod init honeypot && go mod tidy

RUN go build -o honeypot

CMD ["./honeypot"]
