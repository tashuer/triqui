# Triqui

Juego de triqui (tres en raya) para dos jugadores, desarrollado en Python y jugado por consola.

## Descripción

Dos jugadores, **X** y **O**, se turnan para marcar casillas de un tablero de 3x3. Gana quien logre alinear tres marcas propias en una fila, columna o diagonal. Si el tablero se llena sin ganador, la partida termina en empate.

## Requisitos

- Python 3.8 o superior (solo usa la biblioteca estándar).

## Cómo jugar

```bash
python triqui.py
```

Las casillas se numeran del 1 al 9:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

En cada turno, escribe el número de la casilla donde quieres jugar. Al terminar la partida puedes elegir si jugar otra vez.

## Pruebas

```bash
python -m unittest test_triqui.py
```

## Estructura

- `triqui.py`: lógica del juego y bucle principal.
- `test_triqui.py`: pruebas de la lógica (ganador, empate, jugadas inválidas).
