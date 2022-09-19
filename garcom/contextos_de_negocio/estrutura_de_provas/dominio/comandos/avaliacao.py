from dataclasses import dataclass

from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.barramento import Comando

from .....adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao


@dataclass
class CriarAvaliacao(Comando):

    titulo: str
    responsavel: str
    tipo_de_avaliacao: TipoDeAvaliacao
    exercicios: set[ExercicioId]
