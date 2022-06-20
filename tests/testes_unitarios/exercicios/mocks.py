from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)

from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_exercicios import (
    ExercicioAbstratoConsulta
)

from garcom.adaptadores.tipos.tipos import ExercicioId


class RepoExercicioFake(ExercicioAbstratoConsulta):
    """Repositorio de Exercicios Fake."""

    def __init__(self):
        self._exercicios: list[Exercicio] = list()

    def _adicionar(self, exercicio: Exercicio) -> None:
        self._exercicios.append(exercicio)

    def _remover(self, exercicio: Exercicio) -> None:
        self._exercicios.remove(exercicio)

    def consultar_todos(self):
        """Retorna todos os exericios."""
        return self._exercicios

    def consultar_por_id(self, exercicio_id: ExercicioId):
        """Retorna o exericios que corresponde ao id passado."""
        return (
            next((
                exercicio for exercicio in self._exercicios 
                if exercicio_id == exercicio.id
            ))
        )
    
    def adicionar(self, exercicio: Exercicio):
        """Adiciona um novo exericio."""
        self._exercicios.append(exercicio)