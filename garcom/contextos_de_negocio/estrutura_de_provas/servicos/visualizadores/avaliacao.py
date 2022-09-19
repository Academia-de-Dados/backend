from garcom.adaptadores.dominio import Dominio
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.agregados.avaliacao import Avaliacao


def consultar_avaliacoes(
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> list[Avaliacao]:

    with unidade_de_trabalho(Dominio.avaliacao) as uow:
        avaliacoes = uow.repo_consulta.consultar_todos()

    return avaliacoes
