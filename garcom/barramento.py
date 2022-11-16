from abc import ABC
from typing import Union

class Comando(ABC):
    pass


class Evento(ABC):
    pass


Mensagem = Union[Comando, Evento]


class BarramentoDeMensagens:
    """
    O modelo de dominio fica responsável por registrar comandos e eventos,
    enquanto o barramento de mensagens responde esses eventos invocando
    uma nova operação.
    """
    def __init__(
        self, 
        unidade_de_trabalho, 
        manipuladores_de_eventos, 
        manipuladores_de_comandos,
    ):
        self.unidade_de_trabalho = unidade_de_trabalho
        self.manipuladores_de_eventos = manipuladores_de_eventos
        self.manipuladores_de_comandos = manipuladores_de_comandos


    class NaoEUmEventoOuComando(Exception):
        pass


    def manipulador(self, mensagem: Mensagem):
        
        self.resultado_do_comando = None
        self.fila = [mensagem]
        while self.fila:
            mensagem = self.fila.pop(0)

            if isinstance(mensagem, Evento):
                self.manipulador_de_eventos(mensagem)
            
            elif isinstance(mensagem, Comando):
                self.resultado_do_comando = self.manipulador_de_comandos(mensagem)
            
            else:
                raise self.NaoEUmEventoOuComando(
                    'O Objeto não é um evento ou comando.'
            )

        return self.resultado_do_comando
    
    
    def manipulador_de_eventos(self, evento: Evento):
        for manipulador in self.manipuladores_de_eventos.get(type(evento), []):
            manipulador(evento, unidade_de_trabalho=self.unidade_de_trabalho)
            self.fila.extend(self.unidade_de_trabalho.coletar_novos_eventos())
    
    
    def manipulador_de_comandos(self, comando: Comando):
        ...