from typing import Type
from uuid import UUID
from garcom.contextos_de_negocio.agregado import Agregado

from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_exercicios import (
    ExercicioAbstratoConsulta
)


class RepoFake(ExercicioAbstratoConsulta):
    """Repositorio de Exercicios Fake."""

    def __init__(self):
        self._objetos: list[Type[Agregado]] = list()

    def _adicionar(self, objeto: Type[Agregado]) -> None:
        self._objetos.append(objeto)

    def _remover(self, objeto: Type[Agregado]) -> None:
        self._objetos.remove(objeto)

    def consultar_todos(self):
        """Retorna todos os exericios."""
        return self._objetos

    def consultar_por_id(self, objeto_id: UUID):
        """Retorna o exericios que corresponde ao id passado."""
        return (
            next((
                objeto for objeto in self._objetos 
                if objeto_id == objeto.id
            ))
        )
    
    def consultar_todos_por_agregado(self, agregado: Type[Agregado]):

        return [
            objeto for objeto in self._objetos 
            if isinstance(objeto, agregado)
        ]

    def adicionar(self, objeto: Type[Agregado]):
        """Adiciona um novo exericio."""
        self._objetos.append(objeto)