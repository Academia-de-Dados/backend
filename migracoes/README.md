# Migrações de Banco de Dados

A API de operações funciona para os comandos de DDL (Data Definition Language):

* Criação de tabelas (CREATE TABLE)
* Alteração de tabelas (ALTER TABLE)
* Deleção de tabelas (DROP TABLE)

Essas operações devem ser feitas dentro das funções de upgrade() e downgrade(),
geradas automaticamente no arquivo da versão da migração. Agradecimento ao Dunossauro 
(Eduardo Mendes) pela live 211 de migrações.

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

## Gerando migrações automaticas

Para gerar migrações automaticamente é preciso adicionar no arquivo env.py dentro
da pasta migracoes o metadata utilizado nos modelos do código. Depois disso, basta
gerar o comando:

```sh
alembic revision --autogenerate -m "mensagem com descricao do que foi alterado no banco"
```

## Migrações em batch

Se você fizer uma migração online e um acesso for feito nesse meio tempo, a pessoa
pode pegar um período instável do banco. Por que ele vai fazer as operações
linha linha. Para fazer todas as modificações de uma vez, usamos as operações de
batch:

```python
def upgrade() -> None:
    with op.batch_alter_table('nome_da_tabela', schema=None) as batch_op:
        batch_op.alter_column(...)
```

Caso o atributo 'render_as_batch' esteja como True nas configurações do arquivo
.env, ele sempre vai executar em batchs e não é necessário adicionar isso na função
de upgrade.