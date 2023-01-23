from abc import abstractmethod
from sqlalchemy.future import select
from garcom.adaptadores.orm.repositorio import RepositorioAbstrato
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


class UsuariosAbstratoConsulta(RepositorioAbstrato):
    @abstractmethod
    def consultar_todos(self) -> list[Usuario]:
        """Retorna todos os exercicios do banco dados."""
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: UsuarioId) -> Usuario:
        """Retorna o exericios corresponde ao id passado."""
        raise NotImplementedError


class UsuariosRepoConsulta(UsuariosAbstratoConsulta):
    def consultar_todos(self) -> list[Usuario]:
        query = self.session.execute(select(Usuario))
        return query.scalars().all()

    def consultar_por_id(self, id: UsuarioId) -> Usuario:
        return self.session.query(Usuario).filter_by(id=id).first()
