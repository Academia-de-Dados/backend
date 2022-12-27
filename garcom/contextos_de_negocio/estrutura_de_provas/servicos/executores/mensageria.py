from ...dominio.eventos.estrutura_de_provas import EnviarEmail
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)


def enviar_email(
    evento: EnviarEmail, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
):
    """
    Implementar envio de emails
    """
    ...
    
    print(evento)