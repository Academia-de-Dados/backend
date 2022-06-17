from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata
)
from garcom.contextos_de_negocio.estrutura_de_provas.repositorio.repo_consulta.consulta_exercicios import ( # noqa
    ExercicioAbstratoConsulta,
 ) 
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)
from garcom.contextos_de_negocio.estrutura_de_provas.servicos.visualizadores.visualizadores_exercicios import consultar_exercicios


exercicios = [
    Exercicio(
        materia="Matematica",
        assunto="geometria",
        dificuldade="facil",
        enunciado="Quanto é dois mais dois?",
    ),
    Exercicio(
        materia="Portugues",
        assunto="gramatica",
        dificuldade="facil",
        enunciado="Quais os tipos de gramática?",
    )        
]


class ExercicioRepoConultaFake(ExercicioAbstratoConsulta):
    """Repositorio Fake para usar nos testes unitários"""
    
    def __init__(self, exercicios: list[Exercicio] = exercicios) -> None:
        self._exercicios = exercicios

    def consultar_todos(self) -> list[Exercicio]:
        """Implementa uma query fake para buscar todos os exercicios."""
        return self._exercicios
    
    def consultar_por_id(self, id: ExercicioId) -> Exercicio:
        """Implementa uma query fake para busca por id."""
        exercicio = [
            exercicio for exercicio in self._exercicios if exercicio.id == id
        ]

        return exercicio[0]

class UnidadeDeTrabalhoFake(UnidadeDeTrabalhoAbstrata):
    """
    Unidade de Trabalho Fake.

    Classe criada para utilizar nos
    testes.
    """
    def __enter__(self):
        self.repo_consulta = ExercicioRepoConultaFake()
        return super().__enter__()

    def close(self) -> None:
        """Método implementado para testes."""
        pass

    def commit(self) -> None:
        """Método implementado para testes."""
        self.comitado = True

    def rollback(self) -> None:
        """Método implementado para testes."""
        pass


def test_consultar_todos_exercicios():

    uow = UnidadeDeTrabalhoFake()

    buscar_exercicios = consultar_exercicios(uow)
    resultado_exercicios_em_dict = [
        exercicio.converter_para_dicionario() for exercicio in buscar_exercicios
    ]

    exercicio_matematica = {
        'materia': 'Matematica', 
        'assunto': 'geometria', 
        'dificuldade': 'facil', 
        'enunciado': 'Quanto é dois mais dois?', 
        'alternativas': None, 
        'resposta': None, 
        'imagem': None, 
        'multipla_escolha': False, 
        'origem': None,
        'id': exercicios[0].id,
        'data_lancamento': None
    }

    exercicio_portugues = {
        'materia': 'Portugues', 
        'assunto': 'gramatica', 
        'dificuldade': 'facil', 
        'enunciado': 'Quais os tipos de gramática?', 
        'alternativas': None, 
        'resposta': None, 
        'imagem': None, 
        'multipla_escolha': False, 
        'origem': None, 
        'id': exercicios[1].id, 
        'data_lancamento': None
    }

    lista_exericios = [exercicio_matematica, exercicio_portugues]

    assert lista_exericios == resultado_exercicios_em_dict
