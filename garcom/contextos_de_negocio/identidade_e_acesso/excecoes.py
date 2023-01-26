from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class SenhaIncorreta(HTTPException):
    status_code: int
    detail: str


@dataclass
class SenhasDiferentes(HTTPException):
    status_code: int
    detail: str


@dataclass
class EmailJaCadastrado(HTTPException):
    status_code: int
    detail: str
