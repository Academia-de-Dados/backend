import re


class NomeInvalido(Exception):
    pass


class EmailInvalido(Exception):
    pass


class Nome(str):
    def __new__(cls, nome: str):
        if not isinstance(nome, str):
            raise NomeInvalido('Nome deve ser compostos apenas de letras!')

        if len(nome) < 7:
            raise NomeInvalido(
                'Nome muito curto, por favor insira mais caracters!'
            )

        return super().__new__(cls, nome)


class Email(str):
    def __new__(cls, email: str):
        if not isinstance(email, str):
            raise EmailInvalido('Email deve ser composto por um texto!')

        regex = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if not regex.match(email):
            raise EmailInvalido('Formatado de email inválido!')

        return super().__new__(cls, email)
