from garcom.contextos_de_negocio.estrutura_de_provas.dominio.eventos import (
    estrutura_de_provas,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.avaliacao import (
    adicionar_avaliacao,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.mensageria import (
    enviar_email,
)

from ..estrutura_de_provas.dominio.comandos.avaliacao import CriarAvaliacao
from ..estrutura_de_provas.dominio.comandos.exercicio import CriarExercicio
from ..estrutura_de_provas.servicos.executores.exercicios import (
    adicionar_exercicio,
)

MANIPULADORES_ESTRUTURA_DE_PROVAS_EVENTOS = {
    estrutura_de_provas.EnviarEmail: [enviar_email],
    estrutura_de_provas.AvaliacaoCriada: [enviar_email],
}

MANIPULADORES_ESTRUTURA_DE_PROVAS_COMANDOS = {
    CriarExercicio: adicionar_exercicio,
    CriarAvaliacao: adicionar_avaliacao,
}
