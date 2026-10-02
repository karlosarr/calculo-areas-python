"""Funciones para calcular areas de figuras geometricas.

El modulo usa validacion comun para evitar resultados silenciosamente
incorrectos cuando una dimension es cero, negativa o no numerica.
"""

import math
from numbers import Real


def _validar_dimensiones(*dimensiones: Real) -> None:
    """Verifica que todas las dimensiones sean numeros reales positivos."""
    for dimension in dimensiones:
        if isinstance(dimension, bool) or not isinstance(dimension, Real):
            raise TypeError("Las dimensiones deben ser numeros reales.")
        if not math.isfinite(dimension):
            raise ValueError("Las dimensiones deben ser finitas.")
        if dimension <= 0:
            raise ValueError("Las dimensiones deben ser mayores que cero.")


def areaTriangulo(base: Real, altura: Real) -> float:
    """Calcula el area de un triangulo: base por altura dividido entre dos."""
    _validar_dimensiones(base, altura)
    return float(base * altura / 2)


def areaCuadrado(lado: Real) -> float:
    """Calcula el area de un cuadrado elevando su lado al cuadrado."""
    _validar_dimensiones(lado)
    return float(lado**2)


def areaRectangulo(base: Real, altura: Real) -> float:
    """Calcula el area de un rectangulo multiplicando base por altura."""
    _validar_dimensiones(base, altura)
    return float(base * altura)


def areaCirculo(radio: Real) -> float:
    """Calcula el area de un circulo usando pi por radio al cuadrado."""
    _validar_dimensiones(radio)
    return float(math.pi * radio**2)


def areaTrapecio(base_mayor: Real, base_menor: Real, altura: Real) -> float:
    """Calcula el area de un trapecio: promedio de bases por altura."""
    _validar_dimensiones(base_mayor, base_menor, altura)
    return float((base_mayor + base_menor) * altura / 2)


def areaRombo(diagonal_mayor: Real, diagonal_menor: Real) -> float:
    """Calcula el area de un rombo: producto de diagonales dividido entre dos."""
    _validar_dimensiones(diagonal_mayor, diagonal_menor)
    return float(diagonal_mayor * diagonal_menor / 2)


def _solicitar_numero(nombre: str) -> float:
    """Solicita una dimension y repite hasta recibir un numero positivo."""
    while True:
        try:
            valor = float(input(f"Ingrese {nombre} (cm): "))
            _validar_dimensiones(valor)
            return valor
        except (TypeError, ValueError) as error:
            print(f"Entrada no valida: {error}")


def main() -> None:
    """Permite elegir una figura y calcula su area con datos del usuario."""
    opciones = {
        "1": ("triangulo", ("la base", "la altura"), areaTriangulo),
        "2": ("cuadrado", ("el lado",), areaCuadrado),
        "3": ("rectangulo", ("la base", "la altura"), areaRectangulo),
        "4": ("circulo", ("el radio",), areaCirculo),
        "5": (
            "trapecio",
            ("la base mayor", "la base menor", "la altura"),
            areaTrapecio,
        ),
        "6": ("rombo", ("la diagonal mayor", "la diagonal menor"), areaRombo),
    }

    print("Calculadora de areas geometricas")
    print("Ingrese todas las dimensiones en centimetros (cm).")
    print("1. Triangulo\n2. Cuadrado\n3. Rectangulo")
    print("4. Circulo\n5. Trapecio\n6. Rombo\n0. Salir")

    while True:
        opcion = input("\nSeleccione una figura: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            return
        if opcion not in opciones:
            print("Opcion no valida. Seleccione un numero del 0 al 6.")
            continue

        nombre, nombres_dimensiones, funcion = opciones[opcion]
        print(f"Ha seleccionado: {nombre.capitalize()}")
        dimensiones = [_solicitar_numero(nombre_dimension) for nombre_dimension in nombres_dimensiones]
        print(f"El area del {nombre} es: {funcion(*dimensiones):.2f} cm^2")


if __name__ == "__main__":
    main()
