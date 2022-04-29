from typing import Union
from uuid import UUID, uuid4

from sqlalchemy import ARRAY
from sqlalchemy.types import TypeDecorator


class BaseUUID(UUID):
    def __init__(self) -> None:
        _id = str(uuid4())
        super().__init__(_id)


class ExercicioId(BaseUUID):
    pass


class ProvaId(BaseUUID):
    pass


class SET(TypeDecorator):
    """SQL Array type decorado para transformar list em set e vice-versa"""

    impl = ARRAY

    def __init__(self, field_type: Union[list, set]) -> None:
        TypeDecorator.__init__(self, field_type)

    def process_bind_param(self, value: set) -> Union[list, None]:
        if value is None:
            return None

        if isinstance(value, set):
            return list(value)

        raise TypeError(
            f'Coleção de tipo inválido. Esperava {set} e obteve {value}.'
        )

    def process_result_value(self, value: list) -> Union[set, None]:
        if value is not None:
            return set(value)
