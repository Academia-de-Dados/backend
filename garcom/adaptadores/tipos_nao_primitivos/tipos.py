from enum import Enum, EnumMeta
from typing import Union
from uuid import UUID, uuid4

from sqlalchemy import ARRAY
from sqlalchemy.types import TypeDecorator


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class EnumBase(Enum, metaclass=MetaEnum):
    pass


class BaseUUID(UUID):
    """
    Classe base uuid.

    Criada para que o uuid se comporte como
    um ObjectId do pymongo. Qualquer instância
    dessa classe possui um id do tipo uuid4.
    """

    def __init__(self) -> None:
        _id = str(uuid4())
        super().__init__(_id)


class ExercicioId(BaseUUID):
    """Criado para usar como tipo do id de exericios."""

    pass


class AvaliacaoId(BaseUUID):
    """Criado para usar como tipo do id de provas."""

    pass


class UsuarioId(BaseUUID):
    pass


class SET(TypeDecorator):
    """
    Método de conversão.

    Converte um tipo sqlalchemy ARRAY para um tipo SET
    e vise-versa.
    """

    impl = ARRAY

    def __init__(self, field_type: Union[list[str], set[str]]) -> None:
        TypeDecorator.__init__(self, field_type)

    def process_bind_param(self, value: set[str]) -> Union[list[str], None]:
        """Usado para converter de set para lista."""
        if value is None:
            return None

        if isinstance(value, set):
            return list(value)

        raise TypeError(
            f"Coleção de tipo inválido. Esperava {set[str]} e obteve {value}."
        )

    def process_result_value(self, value: list) -> Union[set, None]:
        """Cria um set dos dados de entrada."""
        if value is not None:
            return set(value)
