from garcom.barramento import Evento
from garcom.adaptadores.tipos_nao_primitivos.tipos import ExercicioId

class EnviarEmail(Evento):
    ...


class ExercicioCriado(Evento):
    exercicio_id: ExercicioId