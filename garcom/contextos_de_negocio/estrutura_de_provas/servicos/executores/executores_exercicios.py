from psycopg2 import IntegrityError

from garcom.adaptadores.dominio import Dominio
from garcom.adaptadores.tipos.tipos import ExercicioId
from garcom.camada_de_servicos.unidade_de_trabalho.udt import (
    UnidadeDeTrabalhoAbstrata,
)
from garcom.contextos_de_negocio.estrutura_de_provas.dominio.objeto_de_valor.exercicio import (  # noqa
    Exercicio,
)
from garcom.representacoes import ExercicioModelDominio


def adicionar_exercicio(
    exercicio_model: ExercicioModelDominio,
    unidade_de_trabalho: UnidadeDeTrabalhoAbstrata,
) -> ExercicioId:
    """
    Função executora de adicionar exericicio.

    Essa função se comunica com a aplicação web,
    recebendo os dados e adicionando eles no banco.
    """
    exercicio = Exercicio(
        materia=exercicio_model.materia,
        assunto=exercicio_model.assunto,
        dificuldade=exercicio_model.dificuldade,
        origem=exercicio_model.origem,
        data_lancamento=exercicio_model.data_lancamento,
        enunciado=exercicio_model.enunciado,
        alternativas=exercicio_model.alternativas,
    )

    exercicio_id = exercicio.id

    with unidade_de_trabalho(Dominio.exericios) as uow:
        try:
            exercicio = uow.repo_dominio.adicionar(exercicio)
            uow.commit()

        except IntegrityError as ex:
            print(ex.__cause__)
            uow.rollback()

    return exercicio_id
