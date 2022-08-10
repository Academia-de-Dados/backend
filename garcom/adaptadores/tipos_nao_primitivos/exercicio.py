from ..tipos_nao_primitivos.tipos import EnumBase


class Dificuldade(str, EnumBase):

    facil: str = 'Fácil'
    media: str = 'Média'
    dificil: str = 'Difícil'


class Materia(str, EnumBase):

    matematica: str = 'Matemática'
    portugues: str = 'Português'


class AssuntosMatematica(str, EnumBase):

    estatistica = 'Estatística'
    trigonometria = 'Trigonometria'
    probabilidade = 'Probabilidade'
    algebra_linear = 'Algebra Linear'
    operacoes_basicas = 'Operações Básicas'
    geometria_espacial = 'Geometria Espacial'
    geometria_analitica = 'Geometria Analitica'
    funcao_do_segundo_grau = 'Função do Segundo Grau'
    funcao_do_primeiro_grau = 'Função do Primeiro Grau'
    funcoes_de_ordem_superior = 'Funções de Ordem Superior'


class AssuntosPortugues(str, EnumBase):

    gramatica = 'Gramática'
    literatura = 'Literatura'
