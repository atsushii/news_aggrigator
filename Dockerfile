FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip python3-dev

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt






