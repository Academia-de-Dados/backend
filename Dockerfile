# Staging: base
FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONBREAKPOINT=0

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update -y && \
    apt-get upgrade -y --allow-unauthenticated --no-install-recommends && \
    apt-get install --no-install-recommends curl -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -U pip

# Staging: builder
FROM base as builder

ENV POETRY_VERSION=1.4.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY garcom/ ./garcom/
COPY pyproject.toml poetry.lock .

RUN poetry build -f wheel

# Staging: production
FROM base as production
COPY --from=builder /dist /dist

RUN pip install /dist/*.whl

EXPOSE 8000

COPY gunicorn.conf.py ./
CMD gunicorn garcom.aplicacao.main:app
