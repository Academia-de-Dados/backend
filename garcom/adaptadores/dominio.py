from enum import Enum

from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_exercicios import (  # noqa
    ExercicioRepoConsulta,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_prova import (  # noqa
    ProvaRepoConsulta,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_dominio.dominio_exercicios import (  # noqa
    ExercicioRepoDominio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_dominio.dominio_prova import (  # noqa
    ProvaRepoDominio,
)


class Dominio(Enum):
    """
    Modelo de repositorios.

    Contém os repositorios das entidades e objetos de valor,
    necessários estar aqui para poder ser passados para a
    unidade de trabalho
    """

    exericios = (ExercicioRepoConsulta, ExercicioRepoDominio)
    prova = (ProvaRepoConsulta, ProvaRepoDominio)
