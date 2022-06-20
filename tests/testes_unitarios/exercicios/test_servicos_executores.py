from garcom.representacoes import ExercicioModelDominio
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.executores_exercicios import (
    adicionar_exercicio
)

def test_adicionar_exercicio_consultando_por_todos_exercicios(mock_uow_exercicio):

    exercicio_fake = ExercicioModelDominio(
        materia='Matematica',
        assunto='geometria',
        dificuldade='facil',
        enunciado='Quanto é dois mais dois?',
    )

    # Adicionando exercicio com a função executora
    exercicio_id = adicionar_exercicio(
        exercicio_fake, mock_uow_exercicio
    )

    # Testando se o exercicio foi realmente adicionado
    with mock_uow_exercicio:
        exercicio_adicionado = mock_uow_exercicio.repo_consulta.consultar_todos()

    assert exercicio_adicionado[0].id == exercicio_id


def test_adicionar_exercicio_consultando_por_id(mock_uow_exercicio):

    exercicio_fake = ExercicioModelDominio(
        materia='Matematica',
        assunto='geometria',
        dificuldade='facil',
        enunciado='Quanto é dois mais dois?',
    )

    # Adicionando exercicio com a função executora
    exercicio_id = adicionar_exercicio(
        exercicio_fake, mock_uow_exercicio
    )
    
    # Testando se o exercicio foi realmente adicionado
    with mock_uow_exercicio:
        exercicio_adicionado = mock_uow_exercicio.repo_consulta.consultar_por_id(
            exercicio_id
        )
    
    assert exercicio_adicionado.materia == exercicio_fake.materia