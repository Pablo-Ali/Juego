from elementales import ELEMENTOS, obtener_modificador_elemental


class Jugador:
    def __init__(self, nombre: str, clase: str):
        if clase not in ["guerrero", "mago"]:
            raise ValueError("Clase inválida. Debe ser 'guerrero' o 'mago'.")

        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self._experiencia = 0

        self.vida_maxima = 100
        self.vida = self.vida_maxima

        if clase == "guerrero":
            self.ataque = 15
            self.defensa = 10
            self.poder_magico = 5
            self.resistencia_magica = 5
        else:  # mago
            self.ataque = 5
            self.defensa = 5
            self.poder_magico = 15
            self.resistencia_magica = 10

    def __str__(self):
        return (f"{self.nombre} ({self.clase.capitalize()}, Nivel {self.nivel}) - "
                f"Vida: {self.vida}/{self.vida_maxima} - EXP: {self.experiencia}/{self._experiencia_necesaria()}")

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, valor: int):
        self._experiencia += valor
        while self._experiencia >= self._experiencia_necesaria():
            self._experiencia -= self._experiencia_necesaria()
            self.subir_nivel()

    def _experiencia_necesaria(self) -> int:
        return self.nivel * 100

    def subir_nivel(self):
        self.nivel += 1
        print(f"¡{self.nombre} ha subido al nivel {self.nivel}!")

        # Escalado diferente según la clase
        self.vida_maxima += 20
        if self.clase == "guerrero":
            self.ataque += 4
            self.defensa += 3
            self.poder_magico += 1
            self.resistencia_magica += 1
        else:  # mago
            self.ataque += 1
            self.defensa += 1
            self.poder_magico += 4
            self.resistencia_magica += 3

        self.vida = self.vida_maxima  # Recupera vida

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def recibir_danio(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)

    def atacar_fisico(self, tipo_elemento: str, tipo_enemigo: str) -> int:
        """Devuelve el daño ajustado según el tipo elemental del enemigo."""
        if tipo_elemento not in ELEMENTOS:
            raise ValueError("Elemento inválido para ataque físico")
        modificador = obtener_modificador_elemental(tipo_elemento, tipo_enemigo)
        return int(self.ataque * modificador)

    def atacar_magico(self, tipo_elemento: str, tipo_enemigo: str) -> int:
        """Devuelve el daño ajustado según el tipo elemental del enemigo."""
        if tipo_elemento not in ELEMENTOS:
            raise ValueError("Elemento inválido para ataque mágico")
        modificador = obtener_modificador_elemental(tipo_elemento, tipo_enemigo)
        return int(self.poder_magico * modificador)