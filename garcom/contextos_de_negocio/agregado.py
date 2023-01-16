from abc import ABC
from dataclasses import dataclass, field
from typing import ClassVar, List

from ..barramento import Evento


class Agregado(ABC):
    """
    O atributo eventos deve ser um tipo classvar para que as classes
    que herdam de Agregado não dê erro no
    """

    eventos: List[Evento]

    def adicionar_evento(self, evento: Evento):
        assert issubclass(type(evento), Evento)
        self.eventos.append(evento)
