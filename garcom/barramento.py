from abc import ABC
from typing import Callable, Optional, Union
from uuid import UUID

from garcom.aplicacao.sentry import loggers


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
        unidade_de_trabalho: 'UnidadeDeTrabalho',
        manipuladores_de_eventos: Optional[dict[str, Callable]],
        manipuladores_de_comandos: Optional[dict[str, Callable]],
    ):
        self.unidade_de_trabalho = unidade_de_trabalho
        self.manipuladores_de_eventos = manipuladores_de_eventos
        self.manipuladores_de_comandos = manipuladores_de_comandos

    class NaoEUmEventoOuComando(Exception):
        pass

    def manipulador(self, mensagem: Mensagem) -> UUID:

        self.resultado_do_comando = None
        self.fila = [mensagem]
        while self.fila:
            mensagem = self.fila.pop(0)

            if isinstance(mensagem, Evento):
                self.manipulador_de_eventos(mensagem)

            elif isinstance(mensagem, Comando):
                self.resultado_do_comando = self.manipulador_de_comandos(
                    mensagem
                )

            else:
                raise self.NaoEUmEventoOuComando(
                    'O Objeto não é um evento ou comando.'
                )

        return self.resultado_do_comando

    def manipulador_de_eventos(self, evento: Evento):
        for manipulador in self.manipuladores_de_eventos.get(type(evento), []):
            try:
                loggers.debug(
                    f'Execuntando evento: {evento}, com executor: {manipulador}'
                )

                manipulador(
                    evento, unidade_de_trabalho=self.unidade_de_trabalho
                )
                evento = list(self.unidade_de_trabalho.coletar_novos_eventos())
                self.fila.extend(evento)

            except Exception as e:
                loggers.exception(f'Erro ao executar: {evento}, erro: {e}')

    def manipulador_de_comandos(self, comando: Comando) -> UUID:
        manipulador = self.manipuladores_de_comandos.get(type(comando))
        try:
            loggers.debug(
                f'Execuntando comando: {comando}, com executor: {manipulador}'
            )

            resultado = manipulador(
                comando, unidade_de_trabalho=self.unidade_de_trabalho
            )
            loggers.info(f'Resultado comando: {resultado}')

            evento = list(self.unidade_de_trabalho.coletar_novos_eventos())
            self.fila.extend(evento)

            return resultado

        except Exception as e:
            loggers.exception(f'Erro ao executar: {comando}, erro: {e}')
