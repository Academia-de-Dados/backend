from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.eventos.estrutura_de_provas import EnviarEmail


def enviar_email(
    evento: EnviarEmail, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
):
    """
    Implementar envio de emails

    Crio um arquivo em memoria e salvo, para poder testar se o evento é
    de fato executado.
    """
    ...

    print(evento.mensagem)

    arquivo = open('teste_evento', 'w+')
    arquivo.writelines(evento.mensagem)
    arquivo.close()
