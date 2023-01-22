from tests.testes_unitarios.mocks import RepoFake
from tests.mocks import UnidadeDeTrabalhoFake
from garcom.barramento import BarramentoDeMensagens
from garcom.contextos_de_negocio.barramento.estrutura_de_provas import (
    MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS,
    MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio,
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import Dificuldade, Materia
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio,
)
import os


def test_criar_exercicio_pelo_barramento():

    uow = UnidadeDeTrabalhoFake(repo_consulta=RepoFake())
    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=uow,
        manipuladores_de_eventos=MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS,
    )

    comando_exercicio = CriarExercicio(
        materia=Materia.fisica,
        assunto="Mecânica classica",
        dificuldade=Dificuldade.facil,
        enunciado="Qual a primeira lei de Newton?",
        resposta="Lei da Inêrcia",
    )

    barramento.manipulador(comando_exercicio)

    # verifica se o agregado existe no atributo agregados
    assert uow.repo_consulta.agregados

    # verifica se o agregado é uma instância de Exercicio
    assert isinstance(list(uow.repo_consulta.agregados)[0], Exercicio)

    # verifica se o evento foi de fato executado
    evento = open("teste_evento", "r+")
    assert evento.read() == "Evento executado!"

    # exclui o arquivo depois de testar
    os.remove("teste_evento")
