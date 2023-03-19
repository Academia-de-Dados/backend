from fastapi import FastAPI

from ..contextos_de_negocio.estrutura_de_provas.pontos_de_entrada.api import (
    router_estrutura_de_provas,
)
from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.api import (
    router_usuarios,
)
from garcom.adaptadores.orm.orm import (
    iniciar_mapeamento,
    init_database,
)

app = FastAPI()
app.include_router(router_estrutura_de_provas)
app.include_router(router_usuarios)


@app.get("/")
def rota_hellow():
    return {"mensagem": "Olá Pessoas!"}


@app.on_event("startup")
def on_startup() -> None:
    """Inicializa o banco de dados."""
    
    iniciar_mapeamento()
    init_database()