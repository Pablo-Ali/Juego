from abc import ABC, abstractmethod
from random import choice, random
from elementales import ELEMENTOS
from stats_enemigos import generar_stats_para_enemigo


class Enemigo(ABC):
    def __init__(self, nombre: str, nivel: int):
        self.nombre = nombre
        self.nivel = nivel
        self.elemento = choice(list(ELEMENTOS))

        self.vida = 0
        self.ataque = 0
        self.defensa = 0
        self.poder_magico = 0
        self.resistencia_magica = 0

        self._asignar_estadisticas()

    @abstractmethod
    def _asignar_estadisticas(self):
        """Método que deben implementar las subclases para asignar stats según el tipo."""
        pass

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def recibir_danio(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)

    def atacar_fisico(self) -> int:
        return self.ataque

    def atacar_magico(self) -> int:
        return self.poder_magico

    def __str__(self):
        return (
            f"{self.nombre} (Nivel {self.nivel}) - "
            f"Elemento: {self.elemento} - Vida: {self.vida}"
        )


# -------------------------
# Subclases concretas

class Esbirro(Enemigo):
    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo('esbirro', self.nivel)
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']


class Elite(Enemigo):
    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo('elite', self.nivel)
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']


class Jefe(Enemigo):
    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo('jefe', self.nivel)
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']

    def atacar_fisico(self) -> int:
        probabilidad_critico = 0.1
        if random() < probabilidad_critico:
            print(f"{self.nombre} realizó un GOLPE CRÍTICO FÍSICO!")
            return self.ataque * 2
        return self.ataque

    def atacar_magico(self) -> int:
        probabilidad_critico = 0.1
        if random() < probabilidad_critico:
            print(f"{self.nombre} realizó un GOLPE CRÍTICO MÁGICO!")
            return self.poder_magico * 2
        return self.poder_magico