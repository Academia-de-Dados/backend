from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)

from ...dominio.agregados.exercicio import Exercicio
from ...dominio.comandos.exercicio import CriarExercicio
from ...dominio.eventos.estrutura_de_provas import ExercicioCriado


def adicionar_exercicio(
    comando: CriarExercicio,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> ExercicioId:
    """
    Função executora de adicionar exericicio.

    Essa função se comunica com a aplicação web,
    recebendo os dados e adicionando eles no banco.
    """
    exercicio = Exercicio.criar_novo(comando)
    exercicio_id = exercicio.id

    with unidade_de_trabalho(Dominio.exercicios) as uow:
        try:
            uow.repo_dominio.adicionar(exercicio)
            uow.commit()
            exercicio.adicionar_evento(ExercicioCriado(exercicio_id=exercicio_id))
        except Exception as e:
            print(e)
            uow.rollback()

    return exercicio_id
