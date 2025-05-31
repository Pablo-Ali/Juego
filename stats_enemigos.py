import random

# Stats posibles (sin incluir experiencia)
STAT_KEYS = ['ataque', 'defensa', 'poder_magico', 'resistencia_magica']

# Puntos base por tipo de enemigo
PUNTOS_BASE = {
    'esbirro': 10,
    'elite': 20,
    'jefe': 30
}

# Vida base por tipo de enemigo
VIDA_BASE = {
    'esbirro': 30,
    'elite': 50,
    'jefe': 100
}


def generar_stats_base(tipo_enemigo: str) -> dict:
    """Genera un diccionario de stats base con puntos repartidos aleatoriamente."""
    puntos_disponibles = PUNTOS_BASE.get(tipo_enemigo, 10)
    stats = {clave: 0 for clave in STAT_KEYS}

    for _ in range(puntos_disponibles):
        stat_elegida = random.choice(STAT_KEYS)
        stats[stat_elegida] += 1

    # Vida base con una pequeña variación aleatoria (±5)
    stats['vida'] = VIDA_BASE.get(tipo_enemigo, 30) + random.randint(-5, 5)

    return stats


def escalar_stats(stats: dict, nivel: int) -> dict:
    """Escala las estadísticas según el nivel del enemigo."""
    stats_escalados = {}
    for clave, valor in stats.items():
        if clave == 'vida':
            stats_escalados[clave] = valor + nivel * 5
        else:
            stats_escalados[clave] = valor + nivel * 2
    return stats_escalados


def generar_stats_para_enemigo(tipo_enemigo: str, nivel: int) -> dict:
    """Genera stats completos para un enemigo dado su tipo y nivel."""
    stats_base = generar_stats_base(tipo_enemigo)
    stats_escalados = escalar_stats(stats_base, nivel)
    return stats_escalados