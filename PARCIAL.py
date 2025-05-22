#CODIGO CREADO POR SANTIAGO HERNANDEZ GOMEZ - ID 1012407


class Pelicula:
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo      # Atributo privado para el código
        self.__titulo = titulo      # Atributo privado para el título
        self.__duracion = duracion  # Atributo privado para la duración
        self.__director = director  # Atributo privado para el director
        self.__prestada = prestada  # Atributo privado para estado de préstamo

    #GETTERS
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_duracion(self):
        return self.__duracion

    def get_director(self):
        return self.__director

    def is_prestada(self):
        return self.__prestada # Devuelve True si la película está prestada, False si no

    #SETTERS
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        # Validación básica - Establece la duración en minutos, duración no puede ser negativa
        if duracion >= 0:
            self.__duracion = duracion
        else:
            print("Error: La duración no puede ser negativa")

    def set_director(self, director):
        self.__director = director

    def set_prestada(self, prestada):
        self.__prestada = prestada

    #MÉTODOS DE GESTIÓN#
    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return "La película ha sido prestada con éxito."
        else:
            return "La película ya estaba prestada. No se puede prestar nuevamente."

    def devolver(self):
        if self.__prestada:
            self.__prestada = False
            return "La película ha sido devuelta con éxito."
        else:
            return "La película no estaba prestada. No hay nada que devolver."

    def costo_reproduccion(self, tarifa_por_minuto):

        if tarifa_por_minuto < 0:
            raise ValueError("La tarifa por minuto no puede ser negativa")
        return self.__duracion * tarifa_por_minuto

    #SOBRECARGA DE OPERADORES
    def __str__(self):   #Representación en string de la película.
        estado = "está prestada" if self.__prestada else "no está prestada"
        return (f'La película {self.__codigo} titulada "{self.__titulo}" '
                f'dirigida por {self.__director} dura {self.__duracion} '
                f'minutos y {estado}.')

    def __eq__(self, otra_pelicula):
        if isinstance(otra_pelicula, Pelicula):
            return self.__codigo == otra_pelicula.get_codigo()
        return False