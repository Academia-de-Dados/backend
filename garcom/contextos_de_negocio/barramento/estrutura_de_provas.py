from garcom.contextos_de_negocio.estrutura_de_provas.dominio.eventos import estrutura_de_provas
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.avaliacao import (
    enviar_email, adicionar_avaliacao
)
from ..estrutura_de_provas.dominio.comandos.exercicio import CriarExercicio
from ..estrutura_de_provas.servicos.executores.exercicios import adicionar_exercicio

from ..estrutura_de_provas.dominio.comandos.avaliacao import CriarAvaliacao


MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS = {
    estrutura_de_provas.EnviarEmail: [enviar_email]
}

MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS = {
    CriarExercicio: [adicionar_exercicio],
    CriarAvaliacao: [adicionar_avaliacao],
}