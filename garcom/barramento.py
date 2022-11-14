from abc import ABC


class Comando(ABC):
    pass


class Evento(ABC):
    pass


class OnibusDeMenssagem:
    def __init__(self, unidade_de_trabalho, manipuladores_de_eventos, manipuladores_de_comandos):
        self.unidade_de_trabalho = unidade_de_trabalho
        self.manipuladores_de_eventos = manipuladores_de_eventos
        self.manipuladores_de_comandos = manipuladores_de_comandos

    def manipulador(self):
        ...