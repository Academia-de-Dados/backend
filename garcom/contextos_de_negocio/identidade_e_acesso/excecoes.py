from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class SenhaIncorreta(HTTPException):
    status_code: int
    detail: str