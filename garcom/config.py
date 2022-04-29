from os import getenv


def get_postgres_uri() -> str:
    """- Pega a uri do postgres."""
    usuario = getenv('DB_USER', 'postgres')
    senha = getenv('DB_PASSWORD', 'senha')
    host = getenv('DB_HOST', 'localhost')
    db_name = getenv('DB_NAME', 'postgres')
    port = '5432'

    return f'postgresql://{usuario}:{senha}@{host}:{port}/{db_name}'
