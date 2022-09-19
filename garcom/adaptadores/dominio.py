from enum import Enum

from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_avaliacao import (  # noqa
    AvaliacaoRepoConsulta,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_exercicios import (  # noqa
    ExercicioRepoConsulta,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_dominio.dominio_avaliacao import (  # noqa
    AvaliacaoRepoDominio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_dominio.dominio_exercicios import (  # noqa
    ExercicioRepoDominio,
)


class Dominio(Enum):
    """
    Modelo de repositorios.

    Contém os repositorios das entidades e objetos de valor,
    necessários estar aqui para poder ser passados para a
    unidade de trabalho
    """

    exercicios = (ExercicioRepoConsulta, ExercicioRepoDominio)
    avaliacao = (AvaliacaoRepoConsulta, AvaliacaoRepoDominio)
