CODIGO REALIZADO POR:

SANTIAGO HERNANDEZ GOMEZ - ID 1012407

Descripción del Proyecto
Este sistema de gestión de videotienda implementado en Python permite administrar un catálogo de películas con operaciones básicas como préstamos, devoluciones y cálculo de costos de reproducción. El proyecto demuestra los principios de Programación Orientada a Objetos, incluyendo encapsulamiento, métodos de acceso y sobrecarga de operadores.

Características Principales
- Registro completo de películas con código único, título, duración y director
- Sistema de control de préstamos con validación de estados
- Cálculo automático de costos basado en duración
- Comparación de películas por código único
- Validación de datos integrada

CONTIENE

INFORMACIÓN DE PELÍCULAS
- La película 1002 titulada "Tiburón" dirigida por Steven Spielberg dura 124 minutos y no está prestada.
- La película 1001 titulada "El Padrino" dirigida por Francis Ford Coppola dura 175 minutos y no está prestada.

PRESTAMOS Y DEVOLUCIONES
La película de código 1002
- Acción: La película ha sido prestada con éxito.
- Estado actual: Prestada

COMPARACIÓN DE PELÍCULAS
- ¿La película 'Tiburón' y 'El Padrino II' tienen el mismo código? False

|-----------------------|
|      PELICULA         |
|-----------------------|
| - __codigo: int       |
| - __titulo: str       |
| - __duracion: int     |
| - __director: str     |
| - __prestada: bool    |
|-----------------------|
| + get_codigo()        |
| + set_codigo()        |
| + prestar()           |
| + devolver()          |
| + costo_reproduccion()|
| + __str__()           |
| + __eq__()            |
|-----------------------|

El archivo principal contiene:

- Definición completa de la clase Pelicula
- Implementación de getters y setters
- Métodos de gestión de préstamos
- Cálculo de costos de reproducción
- Ejemplos demostrativos en el bloque principal


INDISPENSABLE TENER
- Python 3.8 o superior instalado

PASOS PARA EJECUTAR
1. Descargue el archivo PARCIAL.py
2. Abra Visual Studio Code y ejecútelo

