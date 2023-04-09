from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.avaliacao import (
    Avaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.avaliacao import (
    consultar_avaliacoes,
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade,
    Materia,
    AssuntosMatematica,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.avaliacao import (
    CriarAvaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio,
)
from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


def test_consultar_todos_avaliacoes(mock_uow):

    # criando exercicios
    comando = CriarExercicio(
        materia=Materia.matematica,
        assunto="Operações Básicas",
        dificuldade=Dificuldade.facil,
        enunciado="Quanto é dois mais dois?",
        resposta="4",
    )

    exercicio = Exercicio.criar_novo(comando)
    with mock_uow:
        mock_uow.repo_consulta.adicionar(exercicio)

    # adicionando avaliacao
    comando = CriarAvaliacao(
        titulo="Avaliação de Matemática",
        responsavel=UsuarioId(),
        tipo_de_avaliacao=TipoDeAvaliacao.avaliacao_ensino_medio,
        exercicios={exercicio.id},
    )

    avaliacao = Avaliacao.criar_avaliacao(comando, {exercicio})
    with mock_uow:
        mock_uow.repo_consulta.adicionar(avaliacao)

    # verificando se o exercicio e a avaliacao estão salvas
    with mock_uow:
        assert mock_uow.repo_consulta.consultar_todos_por_agregado(Exercicio)
        assert mock_uow.repo_consulta.consultar_todos_por_agregado(Avaliacao)

    # Testar a funcao de consulta
    avaliacoes = consultar_avaliacoes(mock_uow)

    for avaliacao in avaliacoes:
        if issubclass(avaliacao.__class__, Avaliacao):
            assert avaliacao.id == avaliacao.id
