FROM python:3.10.2-buster

RUN pip install --upgrade pip

COPY . /code
RUN pip install /code

WORKDIR /code
