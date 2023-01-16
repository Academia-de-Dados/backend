from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.eventos.estrutura_de_provas import EnviarEmail


def enviar_email(
    evento: EnviarEmail, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
):
    """
    Implementar envio de emails
    """
    ...

    print(evento)
