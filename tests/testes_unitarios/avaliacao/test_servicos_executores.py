from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.avaliacao import (
    Avaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.avaliacao import (
    CriarAvaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio,
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade,
    Materia,
    AssuntosMatematica,
)
from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.avaliacao import (
    adicionar_avaliacao,
)


def test_adicionar_avaliacao(mock_uow):

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
        responsavel="Othon",
        tipo_de_avaliacao=TipoDeAvaliacao.avaliacao_ensino_medio,
        exercicios={exercicio.id},
    )

    avaliacao_id = adicionar_avaliacao(comando, mock_uow)

    # verificando se foi realmente adicionado
    with mock_uow:
        avaliacoes = mock_uow.repo_consulta.consultar_todos_por_agregado(Avaliacao)

    assert avaliacoes[0].id == avaliacao_id
