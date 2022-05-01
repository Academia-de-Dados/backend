from os import environ


def get_postgres_uri() -> str:
    """- Pega a uri do postgres."""
    return environ['DATABASE_URI']
