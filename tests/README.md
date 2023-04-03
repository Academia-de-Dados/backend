# Organização dos testes

## Testes Funcionais

São aqueles que testam o que o cliente consome, sem ter acesso a nenhuma 
função ou método do dominio. Consome a api e testa se os dados foram salvos,
deletados, retornados, etc.

## Testes de Integração

São aqueles que testam se a nossa unidade de trabalho está de fato salvando
os dados corretamente. Ou seja, testa a integração da unidade de trabalho
com o sqlalchemy.

## Testes Unitários

São aqueles que testam uma única unidade separada, tem acesso as nossas funções
e métodos. A boa prática diz que o teste unitário tem que ter apenas um assert
por teste, ou seja, ele testa uma única coisa e ponto.