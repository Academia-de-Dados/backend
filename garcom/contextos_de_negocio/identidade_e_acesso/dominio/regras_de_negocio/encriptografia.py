from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from garcom.config import (
    get_secret_key, 
    get_algorithm, 
    get_tipo_de_criptografia, 
    get_tempo_de_expiracao,
)


pwd_contexto = CryptContext(schemes=[get_tipo_de_criptografia()])


def verificar_senha(senha: str, senha_encriptada: str) -> bool:
    return pwd_contexto.verify(senha, senha_encriptada)


def gerar_senha_encriptografada(senha: str) -> str:
    return pwd_contexto.hash(senha)


def criar_token_de_acesso(dado_de_acesso: dict[str, str]) -> str:
    """
    Essa função recebe um dicionario contendo a chave sub e o dado usado para
    identificar o usuario, nesse caso, o email.
    """
    
    dados = dado_de_acesso.copy()
    tempo_de_expiracao = datetime.utcnow() + timedelta(minutes=get_tempo_de_expiracao())
    dados.update({'exp':tempo_de_expiracao})
    
    token_jwt = jwt.encode(
        dados, get_secret_key(), algorithm = get_algorithm()
    )
    
    return token_jwt


def validar_token_de_acesso(token: str) -> str:
    """
    Pega o dado usado para identificar o usuario, que inicialmente foi
    encriptado no token de acesso.
    """
    payload = jwt.decode(
        token,
        get_secret_key(),
        algorithms=[get_algorithm()]
    )
    
    return payload.get('sub')