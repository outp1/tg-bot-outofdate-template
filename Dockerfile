FROM python:3.9.10

RUN mkdir /tgbot
WORKDIR /tgbot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . /tgbot
