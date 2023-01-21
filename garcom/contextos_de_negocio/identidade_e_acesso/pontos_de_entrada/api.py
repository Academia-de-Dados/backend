from fastapi import APIRouter, Response

from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)

router_usuarios = APIRouter()
