#CODIGO CREADO POR SANTIAGO HERNANDEZ GOMEZ - ID 1012407

from PARCIAL import Pelicula

if __name__ == "__main__":
    # Creación de 3 objetos Película
        pelicula1 = Pelicula(1001, "El Padrino", 175, "Francis Ford Coppola")
        pelicula2 = Pelicula(1002, "Tiburón", 124, "Steven Spielberg")
        pelicula3 = Pelicula(1001, "El Padrino II", 200, "Francis Ford Coppola")  # Mismo código que pelicula1

        print("Peliculas creadas:")
        print("Película 1:", pelicula1)
        print("Película 2:", pelicula2)
        print("Película 3:", pelicula3)

        print("\nPrueba de metodos")

        # Probando métodos de préstamo y devolución
        print("\nPrueba de préstamo y devolución")
        print("Película 1 - Estado inicial:", "Prestada" if pelicula1.is_prestada() else "Disponible")
        print("Intentando prestar película 1:", pelicula1.prestar())
        print("Intentando prestar película 1 nuevamente:", pelicula1.prestar())
        print("Intentando devolver película 1:", pelicula1.devolver())
        print("Intentando devolver película 1 nuevamente:", pelicula1.devolver())

        # Probando costo de reproducción
        print("\nPrueba de costo de reproducción")
        tarifa = 20 #20 por minuto
        print(f"Costo de reproducción película 2 ({pelicula2.get_duracion()} min): ${pelicula2.costo_reproduccion(tarifa):.2f}")

        # Probando getters
        print("\nPrueba de getters")
        print("Película 3 - Título:", pelicula3.get_titulo())
        print("Película 3 - Duración:", pelicula3.get_duracion(), "minutos")
        print("Película 3 - Director:", pelicula3.get_director())

        # Probando setters
        print("\nPrueba de setters")
        pelicula2.set_titulo("Tiburón (1975)")
        pelicula2.set_duracion(130)
        print("Película 2 modificada:", pelicula2)

        # Probando comparación entre objetos
        print("\nPrueba de comparación entre objetos")
        print("¿Película 1 == Película 2?", pelicula1 == pelicula2)  # False (códigos diferentes)
        print("¿Película 1 == Película 3?", pelicula1 == pelicula3)  # True (mismo código)
        print("¿Película 1 == 'texto'?", pelicula1 == "texto")  # False (no es instancia de Película)