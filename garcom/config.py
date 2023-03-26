from typing import Optional
from pydantic import BaseSettings


class Configuracoes(BaseSettings):
    """Classe de configuração pegar as envs."""

    database_uri: Optional[str] = None
    database_tests: Optional[str] = None
    dsn_sentry: Optional[str] = None
    secret_key: Optional[str] = None
    algorithm: Optional[str] = None
    tipo_de_criptografia: Optional[str] = None
    tempo_de_expiracao: Optional[str] = None

    class Config:
        """Classe que indica qual o arquivo .env."""

        env_file = '.env'


configs = Configuracoes()


def get_postgres_uri() -> str:
    """Pega a uri do postgres."""
    return configs.database_uri


def get_postgres_tests() -> str:
    """Pega a URI do banco de tests."""
    return configs.database_tests


def get_dsn_sentry() -> str:
    return configs.dsn_sentry


def get_secret_key() -> str:
    return configs.secret_key


def get_algorithm() -> str:
    return configs.algorithm


def get_tipo_de_criptografia() -> str:
    return configs.tipo_de_criptografia


def get_tempo_de_expiracao() -> int:
    return int(configs.tempo_de_expiracao)
