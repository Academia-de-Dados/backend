from datetime import datetime

from pydantic import BaseModel

from garcom.adaptadores.tipos.tipos import ExercicioId


class ExercicioModelConsulta(BaseModel):
    """
    Modelo do objeto Exercicio.

    Criado para usar como tipo de retorno com id
    nas rotas do FastAPI.
    """

    id: ExercicioId
    materia: str
    assunto: str
    dificuldade: str
    enunciado: str
    alternativas: list[str] | None
    origem: str | None
    data_lancamento: datetime | None


class ExercicioModelDominio(BaseModel):
    """
    Modelo do objeto Exercicio.

    Criado para usar como tipo de entrada sem o id nas
    rotas do FastAPI.
    """

    materia: str
    assunto: str
    dificuldade: str
    enunciado: str
    alternativas: list[str] | None
    origem: str | None
    data_lancamento: datetime | None
