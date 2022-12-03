from abc import ABC

from ..barramento import Evento
from dataclasses import dataclass, field


@dataclass
class Agregado(ABC):

    eventos: list[Evento] = field(default_factory=list)

    def adicionar_evento(self, evento: Evento):
        assert issubclass(type(evento), Evento)
        self.eventos.append(evento)
