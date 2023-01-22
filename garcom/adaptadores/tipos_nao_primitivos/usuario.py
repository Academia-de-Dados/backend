import re


class NomeInvalido(Exception):
    pass


class EmailInvalido(Exception):
    pass


class SenhaInvalida(Exception):
    pass


class Nome(str):
    def __new__(cls, nome: str):
        if not isinstance(nome, str):
            raise NomeInvalido("Nome deve ser compostos apenas de letras!")

        if len(nome) < 7:
            raise NomeInvalido("Nome muito curto, por favor insira mais caracters!")

        return super().__new__(cls, nome)


class Email(str):
    def __new__(cls, email: str):
        if not isinstance(email, str):
            raise EmailInvalido("Email deve ser composto por um texto!")

        regex = re.compile(r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
        if not regex.match(email):
            raise EmailInvalido("Formatado de email inválido!")

        return super().__new__(cls, email)


class Senha(str):
    def __new__(cls, senha: str):
        if len(senha) < 8:
            raise SenhaInvalida("Senha muito curta!")

        if not isinstance(senha, str):
            raise SenhaInvalida(
                "Senha deve conter pelo menos um caracter maiusculo e um numérico."
            )

        caracteres_numericos = []
        caracteres_maiusculos = []
        for caracter in list(senha):
            try:
                int(caracter)
                caracteres_numericos.append(caracter)
            except ValueError:
                maiusculo = caracter.upper()
                if caracter == maiusculo:
                    caracteres_maiusculos.append(caracter)

        if len(caracteres_numericos) == 0:
            raise SenhaInvalida("Senha deve conter pelo menos um caracter númerico!")

        if len(caracteres_maiusculos) < 1:
            raise SenhaInvalida("Senha deve conter pelo menos um caracter maiúsculo!")

        return super().__new__(cls, senha)
