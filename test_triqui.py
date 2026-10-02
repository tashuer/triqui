import unittest

from triqui import ganador, jugar, nuevo_tablero, tablero_lleno


class TestTriqui(unittest.TestCase):
    def test_tablero_nuevo_sin_ganador(self):
        tablero = nuevo_tablero()
        self.assertIsNone(ganador(tablero))
        self.assertFalse(tablero_lleno(tablero))

    def test_gana_por_fila(self):
        tablero = list("XXXOO    ")
        self.assertEqual(ganador(tablero), "X")

    def test_gana_por_columna(self):
        tablero = list("XO XO X  ")
        self.assertEqual(ganador(tablero), "X")

    def test_gana_por_diagonal(self):
        tablero = list("OXXXO  XO")
        self.assertEqual(ganador(tablero), "O")

    def test_empate(self):
        tablero = list("XOXXOOOXX")
        self.assertIsNone(ganador(tablero))
        self.assertTrue(tablero_lleno(tablero))

    def test_jugada_valida(self):
        tablero = nuevo_tablero()
        jugar(tablero, 5, "X")
        self.assertEqual(tablero[4], "X")

    def test_casilla_ocupada(self):
        tablero = nuevo_tablero()
        jugar(tablero, 1, "X")
        with self.assertRaises(ValueError):
            jugar(tablero, 1, "O")

    def test_casilla_fuera_de_rango(self):
        tablero = nuevo_tablero()
        with self.assertRaises(ValueError):
            jugar(tablero, 0, "X")
        with self.assertRaises(ValueError):
            jugar(tablero, 10, "X")


if __name__ == "__main__":
    unittest.main()
