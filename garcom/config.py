from pydantic import BaseSettings


class Configuracoes(BaseSettings):
    """Classe de configuração pegar as envs."""

    database_uri: str
    database_tests: str

    class Config:
        """Classe que indica qual o arquivo .env."""

        env_file = '.env'


configs = Configuracoes()


def get_postgres_uri() -> str:
    """- Pega a uri do postgres."""
    return configs.database_uri


def get_postgres_tests() -> str:
    """Pega a URI do banco de tests."""
    return configs.database_tests
