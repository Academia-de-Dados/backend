from dataclasses import asdict, dataclass
from datetime import datetime

from garcom.adaptadores.tipos.tipos import ExercicioId


@dataclass(unsafe_hash=True)
class Exercicio:
    """
    Modelo de exercicio.

    Representado como um objeto de valor,
    para que seja identificado por seus atributos.
    """

    materia: str
    assunto: str
    dificuldade: str
    enunciado: str
    alternativas: list[str] | None = None
    resposta: str | None = None
    imagem: str | None = None
    multipla_escolha: bool = False
    origem: str | None = None
    id: ExercicioId = ExercicioId()
    data_lancamento: datetime | None = None

    def converter_para_dicionario(
        self,
    ) -> dict[str, ExercicioId | str | datetime]:
        """
        Método de conversão.

        Método criado para retornar de forma simples
        um dicionario python com os dados da prova.
        """
        return asdict(self)
