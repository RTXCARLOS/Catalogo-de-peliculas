"""
Mini proyecto 3 - Opción A: Catálogo de películas
Programa de consola para administrar mis películas usando POO.
"""


class Pelicula:
    def __init__(self, codigo, titulo, genero, duracion, clasificacion, vista=False):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self._duracion = 0           #! Atributo protegido
        self.set_duracion(duracion)  # Se guarda usando la validación
        self.clasificacion = clasificacion
        self.vista = vista

    #* Métodos get y set de la duración (encapsulamiento)
    def get_duracion(self):
        return self._duracion

    def set_duracion(self, minutos):
        if self.validar_duracion(minutos):
            self._duracion = minutos
            return True
        return False

    def validar_duracion(self, minutos):
        return minutos > 0

    def marcar_vista(self):
        self.vista = True

    def __str__(self):
        if self.vista:
            estado = "Vista"
        else:
            estado = "Pendiente"
        return (f"Código: {self.codigo}, Título: {self.titulo}, Género: {self.genero}, "
                f"Duración: {self._duracion} min, Clasificación: {self.clasificacion}, Estado: {estado}")

    def mostrar_info(self):
        print(self)


class Catalogo:
    def __init__(self):
        self.peliculas = []   #! Lista de objetos Pelicula

    #* Agregar validando que el código no se repita
    def agregar(self, pelicula):
        if self.buscar_por_codigo(pelicula.codigo) is not None:
            return False
        self.peliculas.append(pelicula)
        return True

    #* Búsquedas
    def buscar_por_codigo(self, codigo):
        for pelicula in self.peliculas:
            if pelicula.codigo.upper() == codigo.upper():
                return pelicula
        return None

    def buscar_por_titulo(self, texto):
        encontradas = []
        for pelicula in self.peliculas:
            if texto.lower() in pelicula.titulo.lower():
                encontradas.append(pelicula)
        return encontradas

    #* Mostrar y filtrar
    def mostrar_todas(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío.")
        for pelicula in self.peliculas:
            pelicula.mostrar_info()

    def mostrar_por_genero(self, genero):
        encontradas = 0
        for pelicula in self.peliculas:
            if pelicula.genero.lower() == genero.lower():
                pelicula.mostrar_info()
                encontradas += 1
        if encontradas == 0:
            print("No hay películas de ese género.")

    def mostrar_pendientes(self):
        for pelicula in self.peliculas:
            if pelicula.vista is False:
                pelicula.mostrar_info()

    #* Eliminar
    def eliminar(self, codigo):
        pelicula = self.buscar_por_codigo(codigo)
        if pelicula is None:
            return False
        self.peliculas.remove(pelicula)
        return True

    #? Cálculos para las estadísticas
    def contar_vistas(self):
        vistas = 0
        for pelicula in self.peliculas:
            if pelicula.vista:
                vistas += 1
        return vistas

    def total_duracion(self):
        suma_minutos = 0
        for pelicula in self.peliculas:
            suma_minutos += pelicula.get_duracion()
        return suma_minutos

    def promedio_duracion(self):
        if len(self.peliculas) == 0:
            return 0
        return self.total_duracion() / len(self.peliculas)

    def pelicula_mas_larga(self):
        mas_larga = self.peliculas[0]
        for pelicula in self.peliculas:
            if pelicula.get_duracion() > mas_larga.get_duracion():
                mas_larga = pelicula
        return mas_larga

    def mostrar_estadisticas(self):
        if len(self.peliculas) == 0:
            print("No hay películas para calcular estadísticas.")
            return
        total = len(self.peliculas)
        vistas = self.contar_vistas()
        print("-----Estadísticas del catálogo-----")
        print(f"Cantidad total de películas: {total}")
        print(f"Películas vistas: {vistas}")
        print(f"Películas pendientes: {total - vistas}")
        print(f"Promedio de duración: {self.promedio_duracion():.2f} min")
        larga = self.pelicula_mas_larga()
        print(f"Película más larga: {larga.titulo} ({larga.get_duracion()} min)")

        print("Películas por género:")
        conteo = {}
        for pelicula in self.peliculas:
            if pelicula.genero in conteo:
                conteo[pelicula.genero] += 1
            else:
                conteo[pelicula.genero] = 1
        for genero in conteo:
            print(f"  - {genero}: {conteo[genero]}")


#* Funciones para pedir datos sin que el programa se caiga
def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: este dato no puede ir vacío.")
        texto = input(mensaje).strip()
    return texto


def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Error: el número debe ser mayor que 0.")
        except ValueError:
            print("Error: debes escribir un número, no letras.")


#! Creación del catálogo con mis películas precargadas
catalogo = Catalogo()
catalogo.agregar(Pelicula("P01", "Iron Man", "Acción", 126, "+12", True))
catalogo.agregar(Pelicula("P02", "Spider-Man", "Acción", 121, "+12", True))
catalogo.agregar(Pelicula("P03", "Avengers: Endgame", "Acción", 181, "+12", False))
catalogo.agregar(Pelicula("P04", "Coyote vs. Acme", "Comedia", 101, "Todo público", False))
catalogo.agregar(Pelicula("P05", "Toy Story", "Animación", 81, "Todo público", True))


if __name__ == "__main__":
    opcion = ""
    while opcion != "0":
        print("\n========== CATÁLOGO DE PELÍCULAS ==========")
        print("1. Agregar película")
        print("2. Mostrar catálogo completo")
        print("3. Buscar película por código")
        print("4. Buscar película por título")
        print("5. Marcar película como vista")
        print("6. Mostrar películas por género")
        print("7. Mostrar películas pendientes")
        print("8. Mostrar estadísticas del catálogo")
        print("9. Eliminar película")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
        print("")

        if opcion == "1":
            print("-----Agregar película-----")
            codigo_ingresado = pedir_texto("Código (ej. P06): ").upper()
            if catalogo.buscar_por_codigo(codigo_ingresado) is not None:
                print("Error: ese código ya existe.")
            else:
                titulo_ingresado = pedir_texto("Título: ")
                genero_ingresado = pedir_texto("Género: ")
                duracion_ingresada = pedir_entero("Duración en minutos: ")
                clasificacion_ingresada = pedir_texto("Clasificación: ")
                nueva = Pelicula(codigo_ingresado, titulo_ingresado, genero_ingresado, duracion_ingresada, clasificacion_ingresada)
                catalogo.agregar(nueva)
                print(f"Película '{titulo_ingresado}' agregada correctamente.")

        elif opcion == "2":
            print("-----Catálogo completo-----")
            catalogo.mostrar_todas()

        elif opcion == "3":
            codigo_ingresado = pedir_texto("Código a buscar: ")
            pelicula_encontrada = catalogo.buscar_por_codigo(codigo_ingresado)
            if pelicula_encontrada is None:
                print("Error: no existe una película con ese código.")
            else:
                pelicula_encontrada.mostrar_info()

        elif opcion == "4":
            titulo_busqueda = pedir_texto("Título o parte del título: ")
            resultados = catalogo.buscar_por_titulo(titulo_busqueda)
            if len(resultados) == 0:
                print("No se encontraron películas con ese título.")
            for pelicula_resultado in resultados:
                pelicula_resultado.mostrar_info()

        elif opcion == "5":
            codigo_ingresado = pedir_texto("Código de la película: ")
            pelicula_encontrada = catalogo.buscar_por_codigo(codigo_ingresado)
            if pelicula_encontrada is None:
                print("Error: no existe una película con ese código.")
            elif pelicula_encontrada.vista:
                print("Esa película ya estaba marcada como vista.")
            else:
                pelicula_encontrada.marcar_vista()
                print(f"'{pelicula_encontrada.titulo}' marcada como vista.")

        elif opcion == "6":
            genero_busqueda = pedir_texto("Género (Acción, Comedia, Animación...): ")
            print(f"-----Películas de {genero_busqueda}-----")
            catalogo.mostrar_por_genero(genero_busqueda)

        elif opcion == "7":
            print("-----Películas pendientes-----")
            catalogo.mostrar_pendientes()

        elif opcion == "8":
            print("-----Estadísticas del catálogo-----")
            catalogo.mostrar_estadisticas()

        elif opcion == "9":
            codigo_ingresado = pedir_texto("Código a eliminar: ")
            if catalogo.eliminar(codigo_ingresado):
                print("Película eliminada.")
            else:
                print("Error: no existe una película con ese código.")

        elif opcion == "0":
            print("¡Gracias por usar el catálogo! Hasta pronto.")

        else:
            print("Error: opción no válida, intenta de nuevo.")