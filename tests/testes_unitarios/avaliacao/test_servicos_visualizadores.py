from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.avaliacao import (
    Avaliacao
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import Exercicio
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.avaliacao import (
    consultar_avaliacoes
)


def test_consultar_todos_avaliacoes(mock_uow):
    
    # Primeiro casdastrar um exercicio
    with mock_uow:
        mock_uow.repo_consulta._adicionar(
            Exercicio(
                materia='Matematica',
                assunto='geometria',
                dificuldade='facil',
                enunciado='Quanto é dois mais dois?',
                resposta='4',
            )
        )
    
    # Cadastrar uma avaliacao
    
    # Testar a funcao de consulta
    ...