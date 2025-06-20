from jugador_model import JugadorModel
from jugador import Jugador

def guardar_jugador(jugador: Jugador):
    JugadorModel.replace(
        nombre=jugador.nombre,
        clase=jugador.clase,
        nivel=jugador.nivel,
        experiencia=jugador.experiencia,
        vida_maxima=jugador.vida_maxima,
        vida_actual=jugador.vida,
        ataque=jugador.ataque,
        defensa=jugador.defensa,
        poder_magico=jugador.poder_magico,
        resistencia_magica=jugador.resistencia_magica
    ).execute()


def cargar_jugador(nombre: str) -> Jugador | None:
    try:
        j = JugadorModel.get(JugadorModel.nombre == nombre)
        jugador = Jugador(nombre=j.nombre, clase=j.clase)
        jugador.nivel = j.nivel
        jugador.experiencia = j.experiencia
        jugador.vida_maxima = j.vida_maxima
        jugador.vida = j.vida_actual  # ← recupera vida actual
        jugador.ataque = j.ataque
        jugador.defensa = j.defensa
        jugador.poder_magico = j.poder_magico
        jugador.resistencia_magica = j.resistencia_magica
        return jugador
    except JugadorModel.DoesNotExist:
        return None
