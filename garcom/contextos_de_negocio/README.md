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