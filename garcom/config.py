from pydantic import BaseSettings


class Configuracoes(BaseSettings):
    """Classe de configuração pegar as envs."""

    database_uri: str

    class Config:
        """Classe que indica qual o arquivo .env."""

        env_file = '.env'


configs = Configuracoes()


def get_postgres_uri() -> str:
    """- Pega a uri do postgres."""
    return configs.database_uri
