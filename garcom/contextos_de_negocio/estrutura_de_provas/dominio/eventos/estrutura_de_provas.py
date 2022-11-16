from dataclasses import dataclass
from garcom.barramento import Evento
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId, AvaliacaoId

class EnviarEmail(Evento):
    ...

@dataclass(fronzen=True)
class ExercicioCriado(Evento):
    exercicio_id: ExercicioId


@dataclass(fronzen=True)
class AvaliacaoCriada(Evento):
    avaliacao_id: AvaliacaoId