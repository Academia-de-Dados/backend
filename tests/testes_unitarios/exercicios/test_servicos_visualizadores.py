from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import Exercicio
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.visualizadores_exercicios import consultar_exercicios


def test_consultar_todos_exercicios(mock_uow_exercicio):

    # Adicionando exercicios
    with mock_uow_exercicio:
        mock_uow_exercicio.repo_consulta._adicionar(
            Exercicio(
                materia='Matematica',
                assunto='geometria',
                dificuldade='facil',
                enunciado='Quanto é dois mais dois?',
            )
        )
        mock_uow_exercicio.repo_consulta._adicionar(
            Exercicio(
                materia='Portugues',
                assunto='gramatica',
                dificuldade='facil',
                enunciado='Qual o nome do acento ?',
            )               
        )
    
    # Consultar um exercicio com a função visualizadora
    exercicios = consultar_exercicios(mock_uow_exercicio)

    assert len(exercicios) == 2