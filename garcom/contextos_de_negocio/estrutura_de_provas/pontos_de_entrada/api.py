from typing import List

from fastapi import APIRouter, Response, Depends

from garcom.adaptadores.tipos_nao_primitivos.tipos import (
    AvaliacaoId,
    ExercicioId,
)
from garcom.barramento import BarramentoDeMensagens
from garcom.camada_de_servicos.unidade_de_trabalho.udt import UnidadeDeTrabalho
from garcom.representacoes import (
    AvaliacaoModelConsulta,
    AvaliacaoModelDominio,
    ExercicioModelConsulta,
    ExercicioModelDominio,
)

from ...barramento.estrutura_de_provas import (
    MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS,
    MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS,
)
from ...estrutura_de_provas.dominio.agregados.avaliacao import Avaliacao
from ..dominio.agregados.exercicio import Exercicio
from ..dominio.comandos.avaliacao import CriarAvaliacao
from ..dominio.comandos.exercicio import CriarExercicio
from ..servicos.visualizadores.avaliacao import consultar_avaliacoes
from ..servicos.visualizadores.exercicios import consultar_exercicios

from garcom.contextos_de_negocio.identidade_e_acesso.pontos_de_entrada.permissoes import (
    usuario_professor
)

router_estrutura_de_provas = APIRouter(tags=['Estrutura de Provas'])


@router_estrutura_de_provas.get(
    '/exercicios', response_model=List[ExercicioModelConsulta], status_code=200
)
def consultar_todos_exercicios() -> List[Exercicio]:
    """
    Rota para consulta de exercicios.

    Instância a unidade de trabalho e chama o método visualizador,
    retornando todos os exercicios salvos no banco de dados.
    """
    unidade_de_trabalho = UnidadeDeTrabalho()
    exercicios = consultar_exercicios(unidade_de_trabalho)

    if not exercicios:
        return Response(status_code=204)

    return exercicios


@router_estrutura_de_provas.post(
    '/exercicios', response_model=ExercicioId, status_code=201
)
def cadastrar_novo_exercicio(exercicio: ExercicioModelDominio) -> ExercicioId:
    """
    Rota de cadastro de exercicios.

    Instância a unidade de trabalho e chama o método de dominio,
    retornando apenas o id do exercicio salvo.
    """
    unidade_de_trabalho = UnidadeDeTrabalho()
    comando = CriarExercicio(
        materia=exercicio.materia,
        assunto=exercicio.assunto,
        dificuldade=exercicio.dificuldade,
        enunciado=exercicio.enunciado,
        alternativas=exercicio.alternativas,
        multipla_escolha=exercicio.multipla_escolha,
        resposta=exercicio.resposta,
        origem=exercicio.origem,
        data_lancamento=exercicio.data_lancamento,
        imagem_enunciado=exercicio.imagem_enunciado,
        imagem_resposta=exercicio.imagem_resposta,
    )

    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)


@router_estrutura_de_provas.get(
    '/avaliacao', response_model=List[AvaliacaoModelConsulta], status_code=200
)
def consultar_todas_avaliacoes() -> List[Avaliacao]:

    unidade_de_trabalho = UnidadeDeTrabalho()
    avaliacoes = consultar_avaliacoes(unidade_de_trabalho)
    if not avaliacoes:
        return Response(status_code=204)

    return avaliacoes


@router_estrutura_de_provas.post(
    '/avaliacao', 
    response_model=AvaliacaoId, 
    status_code=201,
    dependencies=[Depends(usuario_professor)]
)
def cadastrar_nova_avaliacao(avaliacao: AvaliacaoModelDominio) -> AvaliacaoId:

    unidade_de_trabalho = UnidadeDeTrabalho()
    comando = CriarAvaliacao(
        titulo=avaliacao.titulo,
        responsavel=avaliacao.responsavel,
        tipo_de_avaliacao=avaliacao.tipo_avaliacao,
        exercicios=avaliacao.exercicios,
    )

    barramento = BarramentoDeMensagens(
        unidade_de_trabalho=unidade_de_trabalho,
        manipuladores_de_eventos=MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS,
        manipuladores_de_comandos=MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS,
    )

    return barramento.manipulador(mensagem=comando)
