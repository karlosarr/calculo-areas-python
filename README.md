# Aplicacion de areas geometricas
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=karlosarr_calculo-areas-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=karlosarr_calculo-areas-python)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=karlosarr_calculo-areas-python&metric=coverage)](https://sonarcloud.io/summary/new_code?id=karlosarr_calculo-areas-python)

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

Para generar el reporte de cobertura localmente:

```bash
python -m pip install coverage
coverage run --branch -m unittest discover -s . -p "test*.py"
coverage report
coverage xml -o coverage.xml
```

## Integracion continua

El workflow de GitHub Actions en `.github/workflows/ci.yml` ejecuta las
pruebas unitarias, genera `coverage.xml`, valida una cobertura minima del 80%
y envia el reporte a SonarCloud en cada `push` y `pull request`.

## Usar en Google Colab

El notebook `areasGeometricasColab.ipynb` contiene las funciones y las pruebas,
por lo que puede ejecutarse directamente en Google Colab sin subir archivos.

1. Ejecuta el notebook completo.
2. Prueba una funcion:

```python
areaCirculo(5)
```

3. Ejecuta la celda de pruebas unitarias.

Las pruebas cubren casos tipicos, valores positivos cercanos a cero, cero,
negativos y tipos de datos incorrectos. Tambien prueban la seleccion de figuras,
la validacion de entradas y la salida del menu interactivo.
