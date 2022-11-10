from fastapi import FastAPI

from ..contextos_de_negocio.estrutura_de_provas.pontos_de_entrada.api import (
    router_estrutura_de_provas,
)
from ..contextos_de_negocio.estrutura_de_provas.repositorio.orm import orm

app = FastAPI()
app.include_router(router_estrutura_de_provas)


@app.get('/')
def rota_hellow():
    return {'mensagem': 'Olá Pessoas!'}


@app.on_event('startup')
def on_startup() -> None:
    """Inicializa o banco de dados."""
    orm.init_database()
    orm.start_mappers()
