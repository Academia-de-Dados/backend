# Migrações de Banco de Dados

A API de operações funciona para os comandos de DDL (Data Definition Language):

* Criação de tabelas (CREATE TABLE)
* Alteração de tabelas (ALTER TABLE)
* Deleção de tabelas (DROP TABLE)

Essas operações devem ser feitas dentro das funções de upgrade() e downgrade(),
geradas automaticamente no arquivo da versão da migração.

## Criando primeira migração

1. Gera o arquivo de versão da migração, dentro da pasta versions gerada ao iniciar
o alembic.

```sh
alembic revision -m "Criando primeira migração"
```

2. O arquivo de migração vem com duas funções definidas: upgrade() e downgrade().
A função upgrade irá executar a migração criando a tabela, coluna, alterando tabelas e colunas,
etc. A função downgrade faz o contrário, desfaz a migração, voltando o banco de dados 
para o estado anterior ao executar a migração.

3. Depois de escrever seu script de migração para executar é simples:

```sh
alembic upgrade head
```

ou:

```sh
alembic downgrade head
```