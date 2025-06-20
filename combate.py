from jugador import Jugador
from enemigos import Enemigo
from elementales import ELEMENTOS


def turno_jugador(jugador: Jugador, enemigo: Enemigo):
    print("\n--- Tu turno ---")
    print("1. Atacar físico")
    print("2. Atacar mágico")
    print("3. Defender")

    opcion = input("Elige una acción: ").strip()

    if opcion in ["1", "2"]:
        print("Elige tipo elemental:")
        for i, elem in enumerate(ELEMENTOS, 1):
            print(f"{i}. {elem.capitalize()}")
        tipo = input("→ ").strip()
        tipos = list(ELEMENTOS)
        if not tipo.isdigit() or int(tipo) not in range(1, len(tipos)+1):
            print("Tipo inválido. Turno perdido.")
            return

        tipo_elemento = tipos[int(tipo)-1]
        if opcion == "1":
            danio = jugador.atacar_fisico(tipo_elemento, enemigo.elemento)
        else:
            danio = jugador.atacar_magico(tipo_elemento, enemigo.elemento)

        print(f"\nAtacaste con {tipo_elemento} e hiciste {danio} de daño.")
        enemigo.recibir_danio(danio)

    elif opcion == "3":
        print("Te defendiste este turno. Recibirás la mitad de daño.")
        return "defensa"

    else:
        print("Opción inválida. Turno perdido.")
        return


def turno_enemigo(enemigo: Enemigo, jugador: Jugador, jugador_defendiendo: bool):
    print("\n--- Turno del enemigo ---")

    danio = enemigo.elegir_ataque(jugador_elemento=None)  # aún no afecta al jugador por tipo
    tipo = "físico" if danio == enemigo.ataque else "mágico"

    if jugador_defendiendo:
        danio = danio // 2
        print("¡Defendiste! Daño reducido a la mitad.")

    jugador.recibir_danio(danio)
    print(f"{enemigo} usó un ataque {tipo} y causó {danio} de daño.")


def combate(jugador: Jugador, enemigo: Enemigo):
    print(f"\n¡Comienza el combate contra {enemigo.nombre}!")

    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"\n{jugador.nombre}: {jugador.vida}/{jugador.vida_maxima} HP")
        print(f"{enemigo.nombre}: {enemigo.vida} HP")

        defendio = turno_jugador(jugador, enemigo)

        if not enemigo.esta_vivo():
            print(f"\n¡Has derrotado a {enemigo.nombre}!")
            break

        turno_enemigo(enemigo, jugador, defendio == "defensa")

        if not jugador.esta_vivo():
            print(f"\n{jugador.nombre} ha sido derrotado...")

