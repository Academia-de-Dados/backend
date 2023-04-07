from dataclasses import dataclass

from garcom.adaptadores.tipos_nao_primitivos.tipos import (
    ExercicioId,
    UsuarioId,
)
from garcom.barramento import Comando

from .....adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao


@dataclass
class CriarAvaliacao(Comando):

    titulo: str
    responsavel: UsuarioId
    tipo_de_avaliacao: TipoDeAvaliacao
    exercicios: set[ExercicioId]
