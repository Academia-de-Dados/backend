from typing import List

from fastapi import APIRouter

from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)
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
def consultar_todos_exercicios() -> List[Exercicio]:
    """
    Rota para consulta de exercicios.

    Instância a unidade de trabalho e chama o método visualizador,
    retornando todos os exercicios salvos no banco de dados.
    """
    unidade_de_trabalho = UnidadeDeTrabalho()

    exercicio = consultar_exercicios(unidade_de_trabalho)

    return exercicio


@router_estrutura_de_provas.post('/exercicios', response_model=ExercicioId)
def cadastrar_novo_exercicio(exercicio: ExercicioModelDominio) -> ExercicioId:
    """
    Rota de cadastro de exercicios.

    Instância a unidade de trabalho e chama o método de dominio,
    retornando apenas o id do exercicio salvo.
    """
    unidade_de_trabalho = UnidadeDeTrabalho()

    id_exericio = adicionar_exercicio(exercicio, unidade_de_trabalho)

    return id_exericio
