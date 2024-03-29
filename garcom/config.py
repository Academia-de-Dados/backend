from typing import Optional

from pydantic import BaseSettings


class Configuracoes(BaseSettings):
    """Classe de configuração pegar as envs."""

    database_uri: str
    database_tests: str
    dsn_sentry: str
    secret_key: str
    algorithm: str
    tipo_de_criptografia: str
    tempo_de_expiracao: str

    class Config:
        """Classe que indica qual o arquivo .env."""

        env_file = '.env'
        env_file_encoding = 'utf-8'


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
