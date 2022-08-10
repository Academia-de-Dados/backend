from typing import Generator

from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.agregados.exercicio import Exercicio


def consultar_exercicios(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> list[Exercicio]:
    """
    Visualizador de exercicios.

    Se comunica com a aplicação web, retornando os
    exercicios cadastrados no banco de dados.
    """
    with unidade_de_trabalho(Dominio.exercicios) as uow:
        exercicios = uow.repo_consulta.consultar_todos()

    return exercicios


def consultar_exercicio_por_id(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata, exercicio_id: ExercicioId
) -> Exercicio:
    """Consulta um exercicio pelo seu id."""

    with unidade_de_trabalho(Dominio.exercicios) as uow:
        return uow.repo_consulta.consultar_por_id(exercicio_id)


def consultar_exercicios_por_id(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
    exercicios_id: list[ExercicioId],
) -> Generator[Exercicio, None, None]:
    """Consulta mais de um exercicio por id"""

    with unidade_de_trabalho(Dominio.exercicios) as uow:
        for exercicio_id in exercicios_id:
            yield uow.repo_consulta.consultar_por_id(exercicio_id)
