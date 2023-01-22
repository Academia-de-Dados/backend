from fastapi import APIRouter, Response

from garcom.contextos_de_negocio.identidade_e_acesso.dominio.agregados.usuarios import (
    Usuario,
)


router_usuarios = APIRouter(prefix='/usuarios', tags=['Identidade e Acesso'])


@router_usuarios.get(response_model='')
def consultar_usuarios():
    ...


@router_usuarios.get('/{id}')
def consultar_usuario_por_id():
    ...
    

@router_usuarios.post('/signup')
def cadastrar_usuario():
    ...


@router_usuarios.post('/signin')
def logar_usuario():
    ...