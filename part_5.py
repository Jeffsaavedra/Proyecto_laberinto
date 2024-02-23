from readchar import readkey
import os
import random

class Juego:
    def __init__(self, laberinto, posicion_inicial, posicion_final):
        self.laberinto = laberinto
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def crear_laberinto(self):
        filas = self.laberinto
        matriz = [list(fila) for fila in filas]
        return matriz

    def mostrar_laberinto(self, matriz):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
        for fila in matriz:
            print("".join(fila))  # Imprime cada fila del laberinto

    def main_loop(self):
        laberinto_matriz = self.crear_laberinto()
        px, py = self.posicion_inicial

        laberinto_matriz[py][px] = 'P'

        while (px, py) != self.posicion_final:
            self.mostrar_laberinto(laberinto_matriz)
            laberinto_matriz[py][px] = 'P'

            # Leer entrada del usuario
            print("Presiona una tecla de dirección para mover al jugador (q para salir): ")
            movimiento = readkey()

            if movimiento == "q":
                break
            elif movimiento == "w":
                if py - 1 >= 0 and laberinto_matriz[py - 1][px] != '#':
                    laberinto_matriz[py][px] = '.'
                    laberinto_matriz[py - 1][px] = 'P'
                    py -= 1
            elif movimiento == "s":
                if py + 1 < len(laberinto_matriz) and laberinto_matriz[py + 1][px] != '#':
                    laberinto_matriz[py][px] = '.'
                    laberinto_matriz[py + 1][px] = 'P'
                    py += 1
            elif movimiento == "a":
                if px - 1 >= 0 and laberinto_matriz[py][px - 1] != '#':
                    laberinto_matriz[py][px] = '.'
                    laberinto_matriz[py][px - 1] = 'P'
                    px -= 1
            elif movimiento == "d":
                if px + 1 < len(laberinto_matriz[0]) and laberinto_matriz[py][px + 1] != '#':
                    laberinto_matriz[py][px] = '.'
                    laberinto_matriz[py][px + 1] = 'P'
                    px += 1

        self.mostrar_laberinto(laberinto_matriz)

        if (px, py) == self.posicion_final:
            print("\n¡Felicidades! Has escapado del laberinto SNAKE.\n")


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Obtener la lista de archivos de mapas
        archivos_mapas = os.listdir(path_a_mapas)
        # Elegir un archivo al azar
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        # Leer el archivo seleccionado
        with open(path_completo, 'r') as file:
            contenido = file.read()

        # Extraer las posiciones iniciales y finales del archivo
        lineas = contenido.split('\n')
        inicio_x, inicio_y, fin_x, fin_y = map(int, lineas[0].split())
        posicion_inicial = (inicio_x, inicio_y)
        posicion_final = (fin_x, fin_y)

        # Llamar al constructor de la clase base
        super().__init__(lineas[1:22], posicion_inicial, posicion_final)

    # Iniciar el juego desde un archivo
juego_archivo = JuegoArchivo("mapas")
juego_archivo.main_loop()