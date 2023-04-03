# backend

O backend é uma plataforma educacional em desenvolvimento, a ideia é ter uma plaforma
com simulados de provas e um sistema de progresso e estatisticas para o aluno e professor
acompanhar o desempenho e evolução.

**Obs**: O projeto está estrutura para utilizar migrações com alembic, lembre-se sempre que 
for fazer alguma mudança no banco de dados, utilize o alembic!

## Rodando o banco de dados para testes

Sobe dois banco de dados postgres ambos na porta padrão do postgres (5432), 
utilizo um para testes de integração e outro to usando pra testar a api.

```sh
make test-env
```

## Banco de dados docker para testes rápidos

Caso prefira subir um banco solo, basta executar:

```
docker run --name garcom -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:14
```

## Instalando bibliotecas novas

Para instalar as bibliotecas utilize o poetry, desse jeito as dependências
do projeto ficam organizadas no arquivo pyproject.toml. Para instalar é simples:

```sh
poetry add nome_da_biblioteca
```

## Utilizando o poetry para criar um ambiente virtual

Para criar um ambiente virtual rode:

```sh
poetry env use 3.10.2
```

Para ativar o ambiente virtual execute:

```sh
poetry shell
```

## Instalando o projeto

Para instalar esse projeto no ambiente de desenvolvimento, use:

```sh
poetry install --all-extras
```

Para instalar apenas as dependências obrigatórias, remova o argumento --all-extras.