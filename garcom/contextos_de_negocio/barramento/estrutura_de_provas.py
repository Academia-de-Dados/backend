from garcom.contextos_de_negocio.estrutura_de_provas.dominio.eventos import estrutura_de_provas
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.executores.avaliacao import (
    enviar_email
)


MANIPULADORES_ESTRUTURA_DE_PROVAS = {
    estrutura_de_provas.EnviarEmail: [enviar_email]
}