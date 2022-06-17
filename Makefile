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
install:  ## Instala o código localmente (recomendo estar dentro de um ambiente virtual).
	@ pip install -U pip
	@ pip install poetry
	@ pip install .[dev,test,lint]
	@ pre-commit install
	@ gitlint install-hook

## @ dev
format:  ## Formata o código automaticamente (isort e blue).
	@ blue $(SRC_DIRS)
	@ isort $(SRC_DIRS)


.PRHONY: lint cc test
## @ CI
lint:  ## Executa a checagem estático (isort, blue, flake8, pydocstyle e mypy).
	# linters
	@ isort --check --diff $(SRC_DIRS)
	@ blue --check $(SRC_DIRS)
	@ flake8 $(SRC_DIRS)
	@ pydocstyle
	# @ mypy $(SRC_DIRS)

## @ CI
cc:  ## Verifica a complexidade ciclomática do código.
	# cyclomatic complexity
	@ radon cc $(SRC_DIRS) -s
	@ xenon --max-absolute A --max-modules A --max-average A $(SRC_DIRS)

## @ CI
test: ## Executa os teste e mostra a cobertura do código.
	# testing and testing coverage
	@ coverage run --source=$(SRC_DIRS) --module pytest
	@ coverage html
	@ coverage report --fail-under=$(COVERAGE_FAIL_UNDER) --show-missing


.PRHONY: run run-dev

## @ Run
run:  ## Roda a aplicação.
	@ gunicorn $(SRC_DIRS).aplicacao.main:app


## @ Run
run-dev:  ## Roda a aplicação (não executar em produção).
	@ uvicorn $(SRC_DIRS).aplicacao.main:app --reload


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
