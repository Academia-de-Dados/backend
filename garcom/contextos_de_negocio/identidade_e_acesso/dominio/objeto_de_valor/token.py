from dataclasses import dataclass


@dataclass
class InfoToken:
    sub: str
    tempo_de_expiracao: int
