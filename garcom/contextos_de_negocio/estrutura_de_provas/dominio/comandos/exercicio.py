from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from garcom.barramento import Comando

from .....adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade,
    Materia,
)


@dataclass
class CriarExercicio(Comando):
    """Comando para criar exercicio."""

    materia: Materia
    assunto: str
    dificuldade: Dificuldade
    enunciado: str
    alternativas: Optional[list[str]] = None
    multipla_escolha: bool = False
    imagem_enunciado: Optional[str] = None
    imagem_resposta: Optional[str] = None
    resposta: Optional[str] = None
    origem: Optional[str] = None
    data_lancamento: Optional[datetime] = None
