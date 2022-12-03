from dataclasses import dataclass
from garcom.barramento import Evento
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId, AvaliacaoId

@dataclass(frozen=True)
class EnviarEmail(Evento):
    mensagem: str


@dataclass(frozen=True)
class ExercicioCriado(Evento):
    exercicio_id: ExercicioId


@dataclass(frozen=True)
class AvaliacaoCriada(Evento):
    avaliacao_id: AvaliacaoId