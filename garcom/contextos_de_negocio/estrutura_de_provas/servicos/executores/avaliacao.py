from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos_nao_primitivos.tipos import AvaliacaoId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.agregados.avaliacao import Avaliacao
from ...dominio.comandos.avaliacao import CriarAvaliacao
from ..visualizadores.exercicios import consultar_exercicios_por_id
from ...dominio.eventos.estrutura_de_provas import EnviarEmail, AvaliacaoCriada


def adicionar_avaliacao(
    comando: CriarAvaliacao,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> AvaliacaoId:
    """
    Função executora de adicionar avaliacao.
    """

    exercicios = set(
        consultar_exercicios_por_id(unidade_de_trabalho, comando.exercicios)
    )

    avaliacao = Avaliacao.criar_avaliacao(comando, exercicios)

    avaliacao_id = avaliacao.id

    with unidade_de_trabalho(Dominio.avaliacao) as uow:
        try:
            uow.repo_dominio.adicionar(avaliacao)
            uow.commit()
            avaliacao.adicionar_evento(AvaliacaoCriada(avaliacao_id))
        except Exception as e:
            # Adicionar logs
            uow.rollback()
            raise e

    return avaliacao_id


def enviar_email(
    evento: EnviarEmail, unidade_de_trabalho: UnidadeDeTrabalhoAbstrata
):
    """
    Implementar envio de emails
    """
    ...