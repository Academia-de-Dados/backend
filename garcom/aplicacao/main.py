from fastapi import FastAPI

from garcom.contextos_de_negocio.estrutura_de_provas.pontos_de_entrada.api import (  # noqa
    router_estrutura_de_provas,
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.orm import orm

app = FastAPI()

orm.start_mappers()

app.include_router(router_estrutura_de_provas)
