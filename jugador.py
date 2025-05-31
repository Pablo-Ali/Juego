class PersonajeJugador:
    def __init__(self, nombre: str, clase: str):
        self.nombre = nombre
        self.clase = clase  # Por ejemplo: "guerrero" o "mago"
        self.nivel = 1
        self.experiencia = 0
        self.vida_maxima = 100
        self.vida_actual = self.vida_maxima

        # Stats iniciales base según la clase
        if clase == "guerrero":
            self.ataque = 15
            self.defensa = 10
            self.poder_magico = 5
            self.resistencia_magica = 5
        elif clase == "mago":
            self.ataque = 5
            self.defensa = 5
            self.poder_magico = 15
            self.resistencia_magica = 10
        else:
            raise ValueError("Clase de personaje no válida")

    def esta_vivo(self) -> bool:
        return self.vida_actual > 0

    def recibir_danio(self, cantidad: int):
        self.vida_actual = max(0, self.vida_actual - cantidad)

    def atacar_fisico(self) -> int:
        return self.ataque

    def atacar_magico(self) -> int:
        return self.poder_magico

    def ganar_experiencia(self, cantidad: int):
        self.experiencia += cantidad
        if self.experiencia >= self._experiencia_necesaria():
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.vida_maxima += 10
        self.vida_actual = self.vida_maxima
        self.ataque += 2
        self.defensa += 2
        self.poder_magico += 2
        self.resistencia_magica += 2
        print(f"{self.nombre} ha subido a nivel {self.nivel}!")

    def _experiencia_necesaria(self) -> int:
        return self.nivel * 100

    def __str__(self):
        return (f"{self.nombre} (Nivel {self.nivel} - {self.clase}) "
                f"Vida: {self.vida_actual}/{self.vida_maxima} "
                f"Exp: {self.experiencia}/{self._experiencia_necesaria()}")