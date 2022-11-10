# backend

## Rodando o banco de dados para testes

make test-env: sobe dois banco de dados postgres um na porta 5431 e outro
na porta 5432, utilizo um para testes de integração e outro to usando pra testar a api.


## Banco de dados docker para testes rápidos

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
## PEP's

* Tipagem: 
  
* Docstring: https://peps.python.org/pep-0257/


## Padrões de Projeto Utilizado

### Unidade de Trabalho

Padrão de projeto Unidade de Trabalho: permite desacoplar
a camada de serviço da camada de dados. Sem o pradão unidade
de trabalho a api se comunica com três camadas: com o banco
de dados para iniciar uma sessão, com a camada repositório para
inicializar o repositorio sqlalchemy e com a camada de serviço
para fazer solicitações.

A ideia é fazer com que a unidade de trabalho gerencie o estado
do banco de dados, deixando a api flask livre dessa responsabilidade.
Com isso, o flask vai ter apenas duas obrigações:
inicializar uma unidade de trabalho e invocar um serviço.


## Entidades, Objetos de Valor e Agregados
### Entidades

Entidade difere do objeto de valor no quesito de poder ser alterado.
Uma entidade possui igualdade de identidade, ou seja, podemos mudar
seus valores que eles ainda são reconhecidos como a mesma coisa.

Exemplo: Podemos ter uma prova com 5 questoes e outra com 4, ainda assim
ambos ainda vão ser uma prova.

* Tornamos explicito que se trata de uma entidade implementando os métodos
* mágicos __eq__ e __hash__

### Objetos de Valor

Objeto de valor é qualquer objeto de domínio identificado
exclusivamente pelos dados que contém.

Exemplo: Duas provas com as mesmas questões são iguais

* fronzen=True, implementa: __setattr__ e __delattr__
- setattr implementa: exercicio.foo = bar
* Para alterar o id: setattr(Pedido, 'id', 'Novo_id')

## Organização dos testes

### Testes Funcionais

São aqueles que testam o que o cliente consome, sem ter acesso a nenhuma 
função ou método do dominio. Consome a api e testa se os dados foram salvos,
deletados, retornados, etc.

### Testes de Integração

São aqueles que testam se a nossa unidade de trabalho está de fato salvando
os dados corretamente. Ou seja, testa a integração da unidade de trabalho
com o sqlalchemy.

### Testes Unitários

São aqueles que testam uma única unidade separada, tem acesso as nossas funções
e métodos. A boa prática diz que o teste unitário tem que ter apenas um assert
por teste, ou seja, ele testa uma única coisa e ponto.
