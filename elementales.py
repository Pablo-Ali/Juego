"""
La secuencia es:

    Fuego ➝ vence a Aire

    Aire ➝ vence a Tierra

    Tierra ➝ vence a Agua

    Agua ➝ vence a Fuego
"""

ELEMENTOS = {"fuego", "agua", "aire", "tierra"}

# Mapa de debilidades: a quién vence cada uno
DEBILIDADES = {
    "fuego": "aire",
    "aire": "tierra",
    "tierra": "agua",
    "agua": "fuego"
}

def calcular_multiplicador(tipo_ataque: str, tipo_defensor: str) -> float:
    """
    Devuelve un multiplicador de daño según las relaciones elementales.
    - 2.0 si el atacante es fuerte contra el defensor.
    - 0.5 si el atacante es débil contra el defensor.
    - 1.0 si no hay ventaja.
    """
    if tipo_ataque not in ELEMENTOS or tipo_defensor not in ELEMENTOS:
        raise ValueError("Tipo elemental no reconocido.")

    if DEBILIDADES[tipo_ataque] == tipo_defensor:
        return 2.0  # ventaja
    elif DEBILIDADES[tipo_defensor] == tipo_ataque:
        return 0.5  # desventaja
    else:
        return 1.0  # neutral