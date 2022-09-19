from ..tipos_nao_primitivos.tipos import EnumBase


class TipoDeAvaliacao(str, EnumBase):

    simulado_enem = 'Simulado Enem'
    simulado_concurso_publico = 'Simulado Concurso Público'
    avaliacao_universitaria = 'Avaliação Universitária'
    avaliacao_ensino_medio = 'Avaliação Ensino Médio'
    avaliacao_ensino_fundamental = 'Avaliação Ensino Fundamental'
