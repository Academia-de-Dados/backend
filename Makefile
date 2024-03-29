SRC_DIRS := garcom
DC := docker-compose
COVERAGE_FAIL_UNDER := 80

.PRHONY: build up down up logs

## @ docker
docker: build up ## Constroi e sobe a aplicação.

## @ docker
build:  ## Constroi o container docker.
	@ $(DC) build

## @ docker
up:  ## Sobe os containers docker.
	@ $(DC) up -d

## @ docker
down:  ## Desce os containers docker.
	@ $(DC) down --remove-orphans

## @ docker
logs:  ## Mostra os logs do service api do docker-compose.
	@ $(DC) logs --follow api


.PRHONY: install format

## @ dev
install:  ## Instala o código localmente.
	@ poetry install --no-interaction --no-root --with lint --with test --with dev
	@ pre-commit install
	@ gitlint install-hook

## @ dev
format:  ## Formata o código automaticamente (isort e blue).
	@ blue $(SRC_DIRS)
	@ isort $(SRC_DIRS)


.PRHONY: lint test
## @ CI
lint:  ## Executa a checagem estático (isort, blue, flake8, pydocstyle e mypy).
	@ isort --check --diff $(SRC_DIRS)
	@ blue --check $(SRC_DIRS)

## @ CI
test: ## Executa os teste e mostra a cobertura do código.
	pytest \
	  --cov-report=html \
	  --cov-config=pyproject.toml \
	  --cov=$(SRC_DIRS) \
	  --cov-fail-under=$(COVERAGE_FAIL_UNDER) \
	  -vv

test-env:
	@ $(DC) -f docker-compose-testes.yml up


.PRHONY: run run-dev

## @ Run
run:  ## Roda a aplicação.
	@ gunicorn $(SRC_DIRS).aplicacao.main:app


## @ Run
run-dev:  ## Roda a aplicação (não executar em produção).
	@ uvicorn $(SRC_DIRS).aplicacao.main:app --reload

run-compose:
	@ $(DC) -f docker-compose.yml up


.PRHONY: help
help:
	@ python -c \
		'import fileinput, re; \
		off, white, darkcyan = "\033[0m", "\033[1;37m", "\033[36m"; \
		lines = (re.search("([a-zA-Z_-]+):.*?## (.*)$$", line) for line in fileinput.input()); \
        methods = filter(None, lines); \
        template = "  "+darkcyan+"  {:10}"+off+" {}"; \
        formated_methods = sorted(template.format(*method.groups()) for method in methods); \
        print(f"\n  usage: make {darkcyan}<command>\n"); \
        print(f"{white}COMMANDS:"); \
        print("\n".join(formated_methods))\
        ' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
