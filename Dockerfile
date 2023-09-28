FROM python:3.10-alpine3.18
WORKDIR /library

COPY requirements.txt /temp/requirements.txt
COPY library /library

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password our-user

USER our-user
