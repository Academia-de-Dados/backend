from fastapi import FastAPI

from garcom.contextos_de_negocio.identidade_e_acesso.repositorio.orm.usuario import (
    start_mappers_usuario,
)

from ..contextos_de_negocio.estrutura_de_provas.pontos_de_entrada.api import (
    router_estrutura_de_provas,
)
from ..contextos_de_negocio.estrutura_de_provas.repositorio.orm.orm import (
    init_database,
    start_mappers,
)

app = FastAPI()
app.include_router(router_estrutura_de_provas)


@app.get("/")
def rota_hellow():
    return {"mensagem": "Olá Pessoas!"}


@app.on_event("startup")
def on_startup() -> None:
    """Inicializa o banco de dados."""
    init_database()
    start_mappers()
    start_mappers_usuario()
