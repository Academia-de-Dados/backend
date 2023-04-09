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

# Guia rápido para testes com o pytest

**Importante:** Este resumo de testes foi retirado da live de python do Dunossauro, link: (https://www.youtube.com/watch?v=MjQCvJmc31A&t=3955s&ab_channel=EduardoMendes)

## Testes com o Pytest

Antes de iniciar os testes lembre de comentar as variáveis de ambiente para não
mandar nenhum teste para o banco de dados.

### Resumo significado do retorno dos testes:

* . : Passou
* F : Falhou
* x : Falha esperada
* X : Falha esperada, mas não falhou
* s : Pulou (skiped)

### Comandos para rodar os Testes

* comando para rodar os testes e mostrar o nome dos testes:
```sh
pytest -v nome_do_arquivo.py
```

* comando para executar os testes e mostrar as saidas do console:
```sh
pytest -s nome_do_arquivo.py
```

* comando para rodar um teste marcado com @mark.task :
```sh
pytest -m task
```

* comando que mostra o motivo de um teste marcado com skip ter sido pulado:
```sh
pytest -rs nome_do_arquivo.py
```

* comando para rodar com o ipd:
```sh
pytest -m task -s
```

* comando para executar todos os testes deste arquivo:
```sh
pytest tests/test_tasks.py
```

* comando para executar todos os testes da pasta tests:
```sh
pytest
```

* comando para rodar os testes e parar com o pdb assim que dê o primeiro erro:
```sh
pytest --pdb
```

### Tags embutidas do mark

* mark.skip(reason = "Descreva a razão de pular o teste"): Para pular um teste

* mark.skipif(): Para pular um teste em um determinado contexto, Exemplo:

```python
import sys
@mark.skipif(
  sys.platform == "win32",
  reason = "Não funciona no windows"
)
def test_soma_2_linux():
  numero_do_pinguim = 42
  assert soma_mais_dois(numero_do_pinguim) == 42
```

* mark.xfail: É esperado que esse teste falhe em algum contexto. Exemplo:

```python
@mark.xfail(python.version < 3)
def test_xfail_version_python():
  assert brincadeira(20) != 'goiabada'
```

* mark.usefixture(): ..

* mark.parametrize(): Para parametrizar testes, ou seja, rodar o mesmo teste com diferentes
parâmetros. A tupla recebe o params e o resultado esperado. Exemplo:

```python
@mark.parametrize(
  'params, mensagem_esperada',
  [(1,3), (3,5), (5,7)]
)
def test_soma_mais_2(params, mensagem_esperada):
  assert soma_mais_2(params) == mensagem_esperada
```

### Fixtures no Pytest

A fixture é basicamente uma maneira de 'entrar' em um contexto. Ou prover uma ferramenta que precisa
ser executada 'antes' dos testes. Os testes são montados por 4 fases:

1. Setup: Onde montamos as coisas
2. Exercise: Onde chamamos as coisas
3. Assert: Onde verificamos as coisas
4. TearDown: Onde desmontamos as coisas

O pytest oferece fixtures prontas, algumas delas são:

1. capsys e variações: 'espiona' o stdout

```python
def test_output(capsys):
    print('meu print')
    captured = capsys.readouterr()
    assert captured.out == 'meu print\n'
```

2. tempdir: Cria um diretório temporário
3. caplog: 'espiona' logs
4. mokeypatch: Adiciona atributos e métodos a objetos em runtime

Para saber mais sobre as fixtures do pytest, basta rodar:
```sh
pytest --fixtures
```

Exemplo de como criar a sua própria fixture:

```python
from pytest import fixture
from app import create_app

@fixture
def flask_app():
    return create_app()

def teste_com_app(flask_app):
    pass
```