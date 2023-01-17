from abc import ABC
from typing import List

from ..barramento import Evento


class Agregado(ABC):

    eventos: List[Evento]

    def adicionar_evento(self, evento: Evento):
        assert issubclass(type(evento), Evento)
        self.eventos.append(evento)
