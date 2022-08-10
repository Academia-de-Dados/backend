from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.avaliacao import (
    Avaliacao
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.avaliacao import (
    CriarAvaliacao
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade, Materia, AssuntosMatematica
)
from garcom.adaptadores.tipos_nao_primitivos.avaliacao import TipoDeAvaliacao


def test_criar_avaliacao():

    # criando exercicio
    comando = CriarExercicio(
        materia=Materia.matematica,
        assunto='Operações Básicas',
        dificuldade=Dificuldade.facil,
        enunciado='Quanto é dois mais dois?',
        resposta='4'
    )
    exercicio = Exercicio.criar_novo(comando)
    exercicio_id = exercicio.id

    # criando avaliacao
    comando = CriarAvaliacao(
        titulo = 'Avaliação de Matemática',
        responsavel= 'Othon',
        tipo_de_avaliacao=TipoDeAvaliacao.avaliacao_ensino_medio,
        exercicios={exercicio_id}
    )

    avaliacao = Avaliacao.criar_avaliacao(comando, {exercicio})

    assert avaliacao
