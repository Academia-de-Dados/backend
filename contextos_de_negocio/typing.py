from typing import Any, Tuple
from uuid import UUID, uuid4


class BaseUUID(UUID):
    def __init__(self, *args: Tuple[Any]):
        """
        Essa classe faz o UUID se comportar como a classe ObjectId. Exemplos:
        # Gerar um novo uuid :
        >>> MotivoId()
        MotivoId('275619da-a4f9-4832-928d-f532ee1f7ecc')

        # Transformar str em uuid e, se já for uuid, retorna o mesmo valor.=:
        >>> MotivoId('275619da-a4f9-4832-928d-f532ee1f7ecc')
        MotivoId('275619da-a4f9-4832-928d-f532ee1f7ecc')

        # Vamos evitar gerar um id se vc passar None.
          Isso evita várias confusões.
        > MotivoId(None) -> Exception
        """

        if not args:
            _id = str(uuid4())
        elif isinstance(args[0], (UUID, str)) or issubclass(
            self.__class__, BaseUUID
        ):
            _id = str(args[0])
        else:
            raise ValueError(
                f'Você não pode transformar um {args[0]} em um UUID'
            )

        super().__init__(_id)


class ExercicioId(BaseUUID):
    pass


class ProvaId(BaseUUID):
    pass
