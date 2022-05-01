from garcom.adaptadores.dominio import Dominio
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.objeto_de_valor.exercicio import Exercicio


def consultar_exercicios(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> list[Exercicio]:
    """
    Visualizador de exercicios.

    Se comunica com a aplicação web, retornando os
    exercicios cadastrados no banco de dados.
    """
    with unidade_de_trabalho(Dominio.exericios) as uow:
        return uow.repo_consulta.consultar_todos()
