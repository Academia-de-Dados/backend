from abc import abstractmethod

from sqlalchemy.future import select

from garcom.adaptadores.orm.repositorio import RepositorioConsulta
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (  # noqa
    Exercicio,
)


class ExercicioAbstratoConsulta(RepositorioConsulta):
    """
    Abstração do Repositorio.

    Classe que define os métodos que o repositorio
    concreto deve implementar.
    """

    @abstractmethod
    def consultar_todos(self) -> list[Exercicio]:
        """Retorna todos os exercicios do banco dados."""
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: ExercicioId) -> Exercicio:
        """Retorna o exericios corresponde ao id passado."""
        raise NotImplementedError


class ExercicioRepoConsulta(ExercicioAbstratoConsulta):
    """
    Repositorio de consulta concreto.

    Utiliza a sessão do sqlalchemy para implementar
    as consultas no banco de dados.
    """

    def consultar_todos(self) -> list[Exercicio]:
        """Implementa uma query de todos os exercicios."""
        query = self.session.execute(select(Exercicio))
        return query.scalars().all()

    def consultar_por_id(self, id: ExercicioId) -> Exercicio:
        """Implementa uma query de exercicio por id."""
        return self.session.query(Exercicio).filter_by(id=id).first()
