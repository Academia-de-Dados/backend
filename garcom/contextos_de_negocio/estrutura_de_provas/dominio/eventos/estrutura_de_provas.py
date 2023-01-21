from dataclasses import dataclass

from garcom.adaptadores.tipos_nao_primitivos.tipos import (
    AvaliacaoId,
    ExercicioId,
)
from garcom.barramento import Evento


@dataclass(frozen=True)
class EnviarEmail(Evento):
    mensagem: str


@dataclass(frozen=True)
class ExercicioCriado(Evento):
    exercicio_id: ExercicioId
    mensagem: str


@dataclass(frozen=True)
class AvaliacaoCriada(Evento):
    avaliacao_id: AvaliacaoId
    mensagem: str
