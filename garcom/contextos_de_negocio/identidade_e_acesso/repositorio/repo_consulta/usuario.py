from abc import abstractmethod
from sqlalchemy.future import select
from garcom.adaptadores.orm.repositorio import RepositorioAbstrato
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId
from garcom.adaptadores.tipos_nao_primitivos.usuario import Email


class UsuariosAbstratoConsulta(RepositorioAbstrato):
    @abstractmethod
    def consultar_todos(self) -> list[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def consultar_por_id(self, id: UsuarioId) -> Usuario:
        raise NotImplementedError

    @abstractmethod
    def consultar_por_email(self, email: Email) -> Usuario:
        raise NotImplementedError


class UsuariosRepoConsulta(UsuariosAbstratoConsulta):
    def consultar_todos(self) -> list[Usuario]:
        query = self.session.execute(select(Usuario))
        return query.scalars().all()

    def consultar_por_id(self, id: UsuarioId) -> Usuario:
        return self.session.query(Usuario).filter_by(id=id).first()
    
    def consultar_por_email(self, email: Email) -> Usuario:
        return self.session.query(Usuario).filter_by(email=email).first()