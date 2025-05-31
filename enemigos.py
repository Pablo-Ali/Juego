from abc import ABC, abstractmethod
from random import choice, random
from elementales import ELEMENTOS

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
        return f"{self.nombre} (Nivel {self.nivel}) - Elemento: {self.elemento} - Vida: {self.vida}"

# -------------------------
# Subclases concretas

class Esbirro(Enemigo):
    def _asignar_estadisticas(self):
        self.vida = 20 + self.nivel * 5
        self.ataque = 5 + self.nivel * 2
        self.defensa = 3 + self.nivel
        self.poder_magico = 2 + self.nivel
        self.resistencia_magica = 2 + self.nivel

class Elite(Enemigo):
    def _asignar_estadisticas(self):
        self.vida = 40 + self.nivel * 6
        self.ataque = 10 + self.nivel * 2
        self.defensa = 5 + self.nivel * 2
        self.poder_magico = 4 + self.nivel
        self.resistencia_magica = 4 + self.nivel

class Jefe(Enemigo):
    def _asignar_estadisticas(self):
        self.vida = 80 + self.nivel * 8
        self.ataque = 15 + self.nivel * 3
        self.defensa = 10 + self.nivel * 2
        self.poder_magico = 6 + self.nivel * 2
        self.resistencia_magica = 6 + self.nivel * 2

    def atacar_fisico(self) -> int:
        critico = random() < 0.1
        if critico:
            print(f"{self.nombre} realizó un GOLPE CRÍTICO FÍSICO!")
            return self.ataque * 2
        return self.ataque

    def atacar_magico(self) -> int:
        critico = random() < 0.1
        if critico:
            print(f"{self.nombre} realizó un GOLPE CRÍTICO MÁGICO!")
            return self.poder_magico * 2
        return self.poder_magico