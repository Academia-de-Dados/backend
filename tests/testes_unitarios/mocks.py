from typing import Type
from uuid import UUID
from garcom.contextos_de_negocio.agregado import Agregado

from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio


class RepoFake(RepositorioAbstratoDominio):
    """Repositorio de Exercicios Fake."""

    def __init__(self):
        super().__init__(session=None)
        self._objetos: list[Type[Agregado]] = list()

    def _adicionar(self, objeto: Type[Agregado]) -> None:
        self._objetos.append(objeto)

    def _remover(self, objeto: Type[Agregado]) -> None:
        self._objetos.remove(objeto)

    def _buscar_por_id(self, objeto_id: UUID):
        """Retorna o agregado que corresponde ao id passado."""
        return next((objeto for objeto in self._objetos if objeto_id == objeto.id))

    def consultar_por_id(self, objeto_id: UUID):
        return self._buscar_por_id(objeto_id)

    def consultar_todos(self):
        """Retorna todos os exericios."""
        return self._objetos

    def consultar_todos_por_agregado(self, agregado: Type[Agregado]):

        return [objeto for objeto in self._objetos if isinstance(objeto, agregado)]
