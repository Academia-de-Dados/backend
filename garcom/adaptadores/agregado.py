from abc import ABC

from ..barramento import Evento


class Agregado(ABC):

    eventos: list[Evento]

    def adicionar_evento(self, evento: Evento):
        assert issubclass(type(evento), Evento)
        self.eventos.append(evento)