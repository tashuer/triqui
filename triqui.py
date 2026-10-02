"""Triqui (tres en raya) para dos jugadores en consola."""

LINEAS_GANADORAS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
    (0, 4, 8), (2, 4, 6),             # diagonales
)


def nuevo_tablero():
    return [" "] * 9


def mostrar_tablero(tablero):
    filas = []
    for i in range(0, 9, 3):
        filas.append(" " + " | ".join(tablero[i:i + 3]))
    return "\n---+---+---\n".join(filas)


def ganador(tablero):
    """Devuelve 'X' u 'O' si hay ganador, o None."""
    for a, b, c in LINEAS_GANADORAS:
        if tablero[a] != " " and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return None


def tablero_lleno(tablero):
    return " " not in tablero


def jugar(tablero, casilla, jugador):
    """Marca la casilla (1-9). Lanza ValueError si la jugada no es válida."""
    if not 1 <= casilla <= 9:
        raise ValueError("La casilla debe estar entre 1 y 9.")
    if tablero[casilla - 1] != " ":
        raise ValueError("Esa casilla ya está ocupada.")
    tablero[casilla - 1] = jugador


def pedir_casilla(jugador):
    while True:
        entrada = input(f"Turno de {jugador}. Casilla (1-9): ").strip()
        if entrada.isdigit():
            return int(entrada)
        print("Escribe un número del 1 al 9.")


def partida():
    tablero = nuevo_tablero()
    jugador = "X"
    while True:
        print()
        print(mostrar_tablero(tablero))
        print()
        casilla = pedir_casilla(jugador)
        try:
            jugar(tablero, casilla, jugador)
        except ValueError as error:
            print(error)
            continue

        if ganador(tablero):
            print()
            print(mostrar_tablero(tablero))
            print(f"\n¡Ganó {jugador}!")
            return
        if tablero_lleno(tablero):
            print()
            print(mostrar_tablero(tablero))
            print("\nEmpate.")
            return
        jugador = "O" if jugador == "X" else "X"


def main():
    print("=== TRIQUI ===")
    while True:
        partida()
        otra = input("\n¿Jugar otra vez? (s/n): ").strip().lower()
        if otra != "s":
            print("¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
