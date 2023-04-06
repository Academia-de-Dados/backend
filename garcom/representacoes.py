from datetime import datetime
from typing import List, Optional, Set

from pydantic import BaseModel

from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao
from garcom.adaptadores.tipos_nao_primitivos.tipos import (
    AvaliacaoId,
    ExercicioId,
    UsuarioId,
)

from .adaptadores.tipos_nao_primitivos.exercicio import Dificuldade, Materia


class MyBaseModel(BaseModel):
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    class Config:
        """
        O pydantic espera um objeto do tipo dicionario e SQLAlchmey
        retorna um objeto do tipo sqlalchemy sendo incopativel com
        o pydantic. Essa clase configura o modo orm para o pydantic
        aceitar os modelos do sqlalchemy.
        """

        orm_mode = True


class ExercicioModelConsulta(MyBaseModel):
    """
    Modelo do objeto Exercicio.

    Criado para usar como tipo de retorno com id
    nas rotas do FastAPI.
    """

    materia: Materia
    assunto: str
    dificuldade: Dificuldade
    enunciado: str
    resposta: str
    alternativas: Optional[list[str]] = None
    multipla_escolha: bool = False
    imagem_enunciado: Optional[str] = None
    imagem_resposta: Optional[str] = None
    origem: Optional[str] = None
    data_lancamento: Optional[datetime] = None
    id: Optional[ExercicioId] = None


class ExercicioModelDominio(MyBaseModel):
    """
    Modelo do objeto Exercicio.

    Criado para usar como tipo de entrada sem o id nas
    rotas do FastAPI.
    """

    assunto: str
    resposta: str
    enunciado: str
    materia: Materia
    dificuldade: Dificuldade
    alternativas: Optional[list[str]] = None
    multipla_escolha: bool = False
    imagem_enunciado: Optional[str] = None
    imagem_resposta: Optional[str] = None
    origem: Optional[str] = None
    data_lancamento: Optional[datetime] = None


class AvaliacaoModelConsulta(MyBaseModel):
    """
    Por algum motivo o pydantic não aceita que exercicios
    seja um Set, talvez pelo motivo de um json não destinguir
    entre set e dicionario.
    """

    titulo: str
    responsavel: UsuarioId
    tipo_de_avaliacao: TipoDeAvaliacao
    exercicios: List[ExercicioModelConsulta]
    id: Optional[AvaliacaoId] = None


class AvaliacaoModelDominio(MyBaseModel):

    titulo: str
    responsavel: UsuarioId
    tipo_avaliacao: TipoDeAvaliacao
    exercicios: Set[ExercicioId]
