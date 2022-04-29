from datetime import datetime

from pydantic import BaseModel

from garcom.adaptadores.tipos.tipos import ExercicioId


class ExercicioModelConsulta(BaseModel):

    id: ExercicioId
    materia: str
    assunto: str
    dificuldade: str
    origem: str | None
    data_lancamento: datetime | None


class ExercicioModelDominio(BaseModel):

    materia: str
    assunto: str
    dificuldade: str
    origem: str | None
    data_lancamento: datetime | None
