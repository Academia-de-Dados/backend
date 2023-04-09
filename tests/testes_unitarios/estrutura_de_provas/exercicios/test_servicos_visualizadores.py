from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.exercicios import (
    consultar_exercicios,
    consultar_exercicio_por_id,
    consultar_exercicios_por_id,
)


def test_consultar_todos_exercicios(mock_uow):

    # Adicionando exercicios
    with mock_uow:
        mock_uow.repo_consulta._adicionar(
            Exercicio(
                materia="Matematica",
                assunto="geometria",
                dificuldade="facil",
                enunciado="Quanto é dois mais dois?",
                resposta="4",
            )
        )
        mock_uow.repo_consulta._adicionar(
            Exercicio(
                materia="Portugues",
                assunto="gramatica",
                dificuldade="facil",
                enunciado="Qual o nome do ponto: '?' ?",
                resposta="Interrogação",
            )
        )

    # Consultar um exercicio com a função visualizadora
    exercicios = consultar_exercicios(mock_uow)

    assert len(exercicios) == 2


def test_consultar_exercicio_por_id(mock_uow):

    # Adicionando exercicio
    with mock_uow:

        exercicio = Exercicio(
            materia="Matematica",
            assunto="geometria",
            dificuldade="facil",
            enunciado="Quanto é dois mais dois?",
            resposta="4",
        )
        exercicio_id = exercicio.id

        mock_uow.repo_consulta._adicionar(exercicio)

    # Consultando por id
    exercicio_consulta = consultar_exercicio_por_id(mock_uow, exercicio_id)

    assert exercicio == exercicio_consulta


def test_consultar_exercicios_por_id(mock_uow):

    # Adicionando exercicios
    with mock_uow:

        exercicio_matematica = Exercicio(
            materia="Matematica",
            assunto="geometria",
            dificuldade="facil",
            enunciado="Quanto é dois mais dois?",
            resposta="4",
        )

        exercicio_portugues = Exercicio(
            materia="Portugues",
            assunto="gramatica",
            dificuldade="facil",
            enunciado="Qual o nome do ponto: '?' ?",
            resposta="Interrogação",
        )

        exercicio_matematica_id = exercicio_matematica.id
        exercicio_portugues_id = exercicio_portugues.id

        mock_uow.repo_consulta._adicionar(exercicio_matematica)

        mock_uow.repo_consulta._adicionar(exercicio_portugues)

    # Consultando exercicios
    exercicios_consulta = list(
        consultar_exercicios_por_id(
            mock_uow, [exercicio_matematica_id, exercicio_portugues_id]
        )
    )

    assert len(exercicios_consulta) == 2
