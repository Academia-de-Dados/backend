"""
Objeto de valor é qualquer objeto de domínio identificado
exclusivamente pelos dados que contém.

Exemplo: Duas provas com as mesmas questões são iguais

* fronzen=True, implementa: __setattr__ e __delattr__
- setattr implementa: exercicio.foo = bar
* Para alterar o id: setattr(Pedido, 'id', 'Novo_id')
"""

from dataclasses import dataclass
from typing import Optional

@dataclass(unsafe_hash=True)
class Exercicio:
    """
    Dois exercicios com os mesmos dados são iguais.
    unsafe_hash implementa a igualdade por todos os atributos.
    """
    materia: str
    assunto: str
    dificuldade: str
    origem: Optional[str]
    data_lancamento: Optional[str]