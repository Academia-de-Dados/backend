from garcom.adaptadores.dominio import Dominio
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)


def consultar_exercicios(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> list[Exercicio]:

    with unidade_de_trabalho(Dominio.exericios) as uow:
        exercicios = uow.repo_consulta.consultar_todos()

    return exercicios
