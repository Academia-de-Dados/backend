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

    exericios = (ExercicioRepoConsulta, ExercicioRepoDominio)
    prova = (ProvaRepoConsulta, ProvaRepoDominio)
