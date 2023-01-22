from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade,
    Materia,
)
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.barramento import Evento
from garcom.contextos_de_negocio.agregado import Agregado
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio,
)

# from ..regras_de_negocio.exercicio import verificar_qual_o_tipo_enum_do_assunto # noqa


@dataclass
class Exercicio(Agregado):
    """
    Modelo de exercicio.

    Representado como um objeto de valor,
    para que seja identificado por seus atributos.
    """

    resposta: str
    assunto: str
    enunciado: str
    materia: Materia
    dificuldade: Dificuldade
    origem: Optional[str] = None
    multipla_escolha: bool = False
    alternativas: List[str] = None
    id: Optional[ExercicioId] = None
    imagem_resposta: Optional[str] = None
    imagem_enunciado: Optional[str] = None
    data_lancamento: Optional[datetime] = None

    eventos = []

    def __post_init__(self):
        self.id = ExercicioId()

        if self.multipla_escolha and not self.alternativas:
            raise self.AlternativasSaoObrigatoriasEmQuestoesDeMultiplaEscolha(
                "As alternativas devem ser fornecidas para questões de "
                "multipla escolha."
            )

    def __repr__(self):
        return (
            f"Exercicio(enunciando={self.enunciado}, "
            f"materia={self.materia.value}, assunto={self.assunto})"
        )

    def __hash__(self):
        return hash(self.id)

    def para_dicionario(self) -> Dict[str, Any]:
        return {
            "enunciado": self.enunciado,
            "resposta": self.resposta,
            "assunto": self.assunto,
            "materia": self.materia,
            "dificuldade": self.dificuldade,
            "origem": self.origem,
            "multipla_escolha": self.multipla_escolha,
            "alternativas": self.alternativas,
            "id": self.id,
            "imagem_resposta": self.imagem_resposta,
            "imagem_enunciado": self.imagem_enunciado,
            "data_lancamento": self.data_lancamento,
        }

    @classmethod
    def criar_novo(cls, criar_exercicio: CriarExercicio) -> "Exercicio":
        """
        Método de criação do Agregado.

        Método utilizado para criar um novo exercicio,
        toda a regra de negócio deve ser tratada aqui.
        """

        # assunto = verificar_qual_o_tipo_enum_do_assunto(
        #    criar_exercicio.assunto
        # )

        return cls(
            materia=criar_exercicio.materia,
            dificuldade=criar_exercicio.dificuldade,
            enunciado=criar_exercicio.enunciado,
            assunto=criar_exercicio.assunto,
            alternativas=criar_exercicio.alternativas,
            multipla_escolha=criar_exercicio.multipla_escolha,
            resposta=criar_exercicio.resposta,
            imagem_enunciado=criar_exercicio.imagem_enunciado,
            imagem_resposta=criar_exercicio.imagem_resposta,
            origem=criar_exercicio.origem,
            data_lancamento=criar_exercicio.data_lancamento,
        )

    class AlternativasSaoObrigatoriasEmQuestoesDeMultiplaEscolha(Exception):
        pass
