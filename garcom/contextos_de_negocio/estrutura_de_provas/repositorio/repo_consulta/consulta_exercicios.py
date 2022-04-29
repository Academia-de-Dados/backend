from abc import abstractmethod

from sqlalchemy.future import select

from garcom.adaptadores.orm.repositorio import RepositorioConsulta
from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)


class ExercicioAbstratoConsulta(RepositorioConsulta):
    @abstractmethod
    def consultar_todos(self):
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: ExercicioId):
        raise NotImplementedError


class ExercicioRepoConsulta(ExercicioAbstratoConsulta):

    # Implementar as querys aqui

    def consultar_todos(self) -> list[Exercicio]:
        # return self.session.query(Exercicio).all()
        query = self.session.execute(select(Exercicio))
        result = query.scalars().all()
        return result

    def consultar_por_id(self, id: ExercicioId) -> Exercicio:
        return self.session.query(Exercicio).filter_by(id=id).first()
