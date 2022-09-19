FROM python:3.10-slim

ENV PYTHONUNBUFFERED=true

# Dependencias necessarias para instalar o poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3.10 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    git config --global url."https://github.com/".insteadOf git://github.com/ && \
    poetry config virtualenvs.create false && \
    poetry config installer.parallel false

RUN mkdir -p /app

WORKDIR /app
EXPOSE 8000

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . /app