"""Pruebas unitarias de las funciones de areas geometricas."""

import math
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from areasGeometricas import (
    areaCirculo,
    areaCuadrado,
    areaRectangulo,
    areaRombo,
    areaTrapecio,
    areaTriangulo,
    main,
)


class TestAreaTriangulo(unittest.TestCase):
    """Pruebas para areaTriangulo."""

    def test_caso_tipico(self):
        self.assertEqual(areaTriangulo(10, 4), 20.0)

    def test_valores_cercanos_a_cero(self):
        self.assertAlmostEqual(areaTriangulo(0.0001, 0.0002), 0.00000001)

    def test_rechaza_cero_y_negativos(self):
        for dimensiones in ((0, 4), (-1, 4), (10, 0)):
            with self.subTest(dimensiones=dimensiones):
                with self.assertRaises(ValueError):
                    areaTriangulo(*dimensiones)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaTriangulo("10", 4)


class TestAreaCuadrado(unittest.TestCase):
    """Pruebas para areaCuadrado."""

    def test_caso_tipico(self):
        self.assertEqual(areaCuadrado(5), 25.0)

    def test_valor_cercano_a_cero(self):
        self.assertAlmostEqual(areaCuadrado(0.0001), 0.00000001)

    def test_rechaza_cero_y_negativo(self):
        for lado in (0, -3):
            with self.subTest(lado=lado):
                with self.assertRaises(ValueError):
                    areaCuadrado(lado)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaCuadrado(None)


class TestAreaRectangulo(unittest.TestCase):
    """Pruebas para areaRectangulo."""

    def test_caso_tipico(self):
        self.assertEqual(areaRectangulo(8, 3), 24.0)

    def test_valores_cercanos_a_cero(self):
        self.assertAlmostEqual(areaRectangulo(0.0001, 0.0002), 0.00000002)

    def test_rechaza_cero_y_negativos(self):
        for dimensiones in ((0, 3), (-2, 3), (8, 0)):
            with self.subTest(dimensiones=dimensiones):
                with self.assertRaises(ValueError):
                    areaRectangulo(*dimensiones)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaRectangulo(8, "3")


class TestAreaCirculo(unittest.TestCase):
    """Pruebas para areaCirculo."""

    def test_caso_tipico(self):
        self.assertAlmostEqual(areaCirculo(3), 9 * math.pi)

    def test_valor_cercano_a_cero(self):
        self.assertAlmostEqual(areaCirculo(0.0001), math.pi * 0.00000001)

    def test_rechaza_cero_y_negativo(self):
        for radio in (0, -3):
            with self.subTest(radio=radio):
                with self.assertRaises(ValueError):
                    areaCirculo(radio)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaCirculo("3")


class TestAreaTrapecio(unittest.TestCase):
    """Pruebas para areaTrapecio."""

    def test_caso_tipico(self):
        self.assertEqual(areaTrapecio(10, 6, 4), 32.0)

    def test_valores_cercanos_a_cero(self):
        self.assertAlmostEqual(areaTrapecio(0.0001, 0.0002, 0.0003), 0.000000045)

    def test_rechaza_cero_y_negativos(self):
        for dimensiones in ((0, 6, 4), (10, -6, 4), (10, 6, 0)):
            with self.subTest(dimensiones=dimensiones):
                with self.assertRaises(ValueError):
                    areaTrapecio(*dimensiones)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaTrapecio(10, 6, "4")


class TestAreaRombo(unittest.TestCase):
    """Pruebas para areaRombo."""

    def test_caso_tipico(self):
        self.assertEqual(areaRombo(10, 6), 30.0)

    def test_valores_cercanos_a_cero(self):
        self.assertAlmostEqual(areaRombo(0.0001, 0.0002), 0.00000001)

    def test_rechaza_cero_y_negativos(self):
        for dimensiones in ((0, 6), (-10, 6), (10, 0)):
            with self.subTest(dimensiones=dimensiones):
                with self.assertRaises(ValueError):
                    areaRombo(*dimensiones)

    def test_rechaza_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            areaRombo(10, [])


class TestMenuPrincipal(unittest.TestCase):
    """Pruebas del menu interactivo y la confirmacion de figura."""

    @patch("builtins.input", side_effect=["1", "10", "4", "0"])
    def test_muestra_figura_seleccionada_y_area(self, entrada_simulada):
        salida = StringIO()
        with redirect_stdout(salida):
            main()

        self.assertIn("Ha seleccionado: Triangulo", salida.getvalue())
        self.assertIn("El area del triangulo es: 20.00 cm^2", salida.getvalue())

    @patch("builtins.input", side_effect=["9", "0"])
    def test_maneja_opcion_invalida_y_permite_salir(self, entrada_simulada):
        salida = StringIO()
        with redirect_stdout(salida):
            main()

        self.assertIn("Opcion no valida", salida.getvalue())
        self.assertIn("Programa finalizado", salida.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
