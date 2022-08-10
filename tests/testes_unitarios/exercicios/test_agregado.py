from pytest import raises
#from garcom.contextos_de_negocio.estrutura_de_provas.execessoes import AssuntoNaoEncontrado
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.agregados.exercicio import (
    Exercicio
)
from garcom.adaptadores.tipos_nao_primitivos.exercicio import (
    Dificuldade, Materia
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.comandos.exercicio import (
    CriarExercicio
)


def test_criar_exercicio_retorna_erro_se_o_for_multipla_escolha_e_nao_tiver_alternativas():

    comando = CriarExercicio(
        materia=Materia.matematica,
        assunto='Operações Básicas',
        dificuldade=Dificuldade.facil,
        enunciado='Quanto é dois mais dois?',
        resposta='4',
        multipla_escolha=True
    )

    with raises(
        Exercicio.AlternativasSaoObrigatoriasEmQuestoesDeMultiplaEscolha
    ) as e:
        Exercicio.criar_novo(comando)
    
    texto_de_erro = (
        'As alternativas devem ser fornecidas para questões de multipla escolha.'
    )
    
    assert texto_de_erro in str(e.value)