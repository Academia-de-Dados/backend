# Aqui fica o router da api FastApi
from typing import List

from adaptadores.tipos.tipos import ExercicioId
from fastapi import APIRouter

from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.executores_exercicios import (  # noqa
    adicionar_exercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.visualizadores_exercicios import (  # noqa
    consultar_exercicios,
)
from garcom.representacoes import ExercicioModelConsulta, ExercicioModelDominio

router_estrutura_de_provas = APIRouter()


@router_estrutura_de_provas.get(
    '/exercicios', response_model=List[ExercicioModelConsulta]
)
def consultar_todos_exercicios() -> List[ExercicioModelConsulta]:

    unidade_de_trabalho = UnidadeDeTrabalho()

    exercicio = consultar_exercicios(unidade_de_trabalho)

    return exercicio


@router_estrutura_de_provas.post('/exercicios', response_model=ExercicioId)
def cadastrar_novo_exercicio(exercicio: ExercicioModelDominio) -> ExercicioId:

    unidade_de_trabalho = UnidadeDeTrabalho()

    id_exericio = adicionar_exercicio(exercicio, unidade_de_trabalho)

    return id_exericio
