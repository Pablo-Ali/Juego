from abc import ABC, abstractmethod
from random import choice, random
from elementales import ELEMENTOS
from stats_enemigos import generar_stats_para_enemigo


class Enemigo(ABC):
    def __init__(self, nivel: int):
        self.nivel = nivel
        self.elemento = choice(list(ELEMENTOS))
        self.vida = 0
        self.ataque = 0
        self.defensa = 0
        self.poder_magico = 0
        self.resistencia_magica = 0
        self.nombre = self._generar_nombre()
        self._asignar_estadisticas()

    @abstractmethod
    def tipo(self) -> str:
        """Tipo textual del enemigo (para el nombre)"""
        pass

    def _generar_nombre(self) -> str:
        tipo = self.tipo().capitalize()
        elemento = self.elemento.capitalize()
        return f"{tipo} de {elemento}"

    @abstractmethod
    def _asignar_estadisticas(self):
        pass

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def recibir_danio(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)

    def atacar(self) -> int:
        if self.ataque > self.poder_magico:
            return self._ataque_fisico_prob()
        else:
            return self._ataque_magico_prob()

    def _ataque_fisico_prob(self) -> int:
        return self.ataque if random() < 0.7 else self.poder_magico

    def _ataque_magico_prob(self) -> int:
        return self.poder_magico if random() < 0.7 else self.ataque

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel}) - Vida: {self.vida}"


class Esbirro(Enemigo):
    def tipo(self) -> str:
        return "esbirro"

    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo("esbirro", self.nivel)
        self._asignar_stats_desde_dict(stats)

    def _asignar_stats_desde_dict(self, stats: dict):
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']


class Elite(Enemigo):
    def tipo(self) -> str:
        return "élite"

    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo("elite", self.nivel)
        self._asignar_stats_desde_dict(stats)

    def _asignar_stats_desde_dict(self, stats: dict):
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']


class Jefe(Enemigo):
    def tipo(self) -> str:
        return "jefe"

    def _asignar_estadisticas(self):
        stats = generar_stats_para_enemigo("jefe", self.nivel)
        self._asignar_stats_desde_dict(stats)

    def _asignar_stats_desde_dict(self, stats: dict):
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.poder_magico = stats['poder_magico']
        self.resistencia_magica = stats['resistencia_magica']

    def _ataque_fisico_prob(self) -> int:
        critico = random() < 0.1
        danio = self.ataque if random() < 0.7 else self.poder_magico
        if critico:
            print(f"{self.nombre} hizo un GOLPE CRÍTICO físico!")
            return danio * 2
        return danio

    def _ataque_magico_prob(self) -> int:
        critico = random() < 0.1
        danio = self.poder_magico if random() < 0.7 else self.ataque
        if critico:
            print(f"{self.nombre} lanzó un HECHIZO CRÍTICO mágico!")
            return danio * 2
        return danio