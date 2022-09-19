from typing import Any
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata
)


class UnidadeDeTrabalhoFake(UnidadeDeTrabalhoAbstrata):
    """
    Unidade de Trabalho Fake.

    Classe criada para utilizar nos
    testes.
    """

    def __init__(self, repo_consulta):
        self.__repo_consulta = repo_consulta
        self.__repo_dominio = repo_consulta

    def __call__(self, *args: list[Any], **kwargs: dict[Any, Any]):
        """
        Método mágico dunder call.

        Utilizado para implementar o operador
        de chamada de função. Atribui aos atributos
        de consulta e dominio o tipo de repositório
        correspondente.
        """       
        return self

    def __enter__(self):
        """
        Método dunder enter.

        Utilizado para retornar o mock dos repositorios.
        """
        self.repo_consulta = self.__repo_consulta
        self.repo_dominio = self.__repo_dominio
        return super().__enter__()

    def close(self) -> None:
        """Método implementado para testes."""
        pass

    def commit(self) -> None:
        """Método implementado para testes."""
        self.comitado = True

    def rollback(self) -> None:
        """Método implementado para testes."""
        pass
