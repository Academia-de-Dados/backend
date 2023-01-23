from garcom.adaptadores.orm.repositorio import RepositorioAbstratoDominio
from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import UsuarioId


class UsuariosRepoDominio(RepositorioAbstratoDominio):
    def _adicionar(self, usuario: Usuario) -> None:
        self.session.add(usuario)

    def _remover(self) -> None:
        pass

    def _buscar_por_id(self, usuario_id: UsuarioId) -> None:
        pass
