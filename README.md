# Aplicacion de areas geometricas

Proyecto en Python para demostrar la implementacion y prueba de funciones de calculo de areas. Incluye seis figuras:

- Triangulo
- Cuadrado
- Rectangulo
- Circulo
- Trapecio
- Rombo

Cada funcion acepta dimensiones numericas reales estrictamente positivas. Si recibe cero, un valor negativo, un valor infinito, `bool` o un tipo no numerico, genera una excepcion explicita.

## Ejecutar en VS Code o localmente

Desde esta carpeta, ejecuta:

```bash
python -m unittest -v
```

La salida debe indicar 26 pruebas exitosas.

## Integracion continua

El workflow de GitHub Actions en `.github/workflows/tests.yml` ejecuta las
pruebas unitarias automaticamente con Python 3.12 en cada `push` y `pull request`.

## Usar en Google Colab

El notebook `areasGeometricasColab.ipynb` importa las funciones de
`areasGeometricas.py`, muestra ejemplos y ejecuta el archivo de pruebas.

1. Sube `areasGeometricas.py` y `testAreasGeometricas.py` al entorno de Colab, o clona este proyecto.
2. Ejecuta el notebook completo, o ejecuta en una celda:

```python
%run areasGeometricas.py
```

3. Prueba una funcion:

```python
areaCirculo(5)
```

4. Ejecuta las pruebas unitarias en otra celda:

```python
!python -m unittest -v testAreasGeometricas.py
```

Tambien puedes ejecutar las pruebas directamente desde una celda Python:

```python
import unittest
from testAreasGeometricas import *

resultado = unittest.TextTestRunner(verbosity=2).run(
    unittest.defaultTestLoader.loadTestsFromModule(__import__("testAreasGeometricas"))
)
```

Las pruebas cubren casos tipicos, valores positivos cercanos a cero, cero,
negativos y tipos de datos incorrectos. Tambien prueban la seleccion de figuras,
la validacion de entradas y la salida del menu interactivo.
