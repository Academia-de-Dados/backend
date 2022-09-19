from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.exercicios import (
    adicionar_exercicio
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade, Materia, AssuntosMatematica
)


def test_adicionar_exercicio(mock_uow):

    comando = CriarExercicio(
        materia=Materia.matematica,
        assunto='Operações Básicas',
        dificuldade=Dificuldade.facil,
        enunciado='Quanto é dois mais dois?',
        resposta='4'
    )

    # Adicionando exercicio com a função executora
    exercicio_id = adicionar_exercicio(
        comando, mock_uow
    )

    # Testando se o exercicio foi realmente adicionado
    with mock_uow:
        exercicio_adicionado = mock_uow.repo_consulta.consultar_todos()

    assert exercicio_adicionado[0].id == exercicio_id