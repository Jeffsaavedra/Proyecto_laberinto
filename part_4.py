from readchar import readkey, key
import os
import time

# Mapa del laberinto
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Función para convertir el mapa en una matriz de caracteres
def crear_laberinto(laberinto_str):
    filas = laberinto_str.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

# Función para limpiar la pantalla y mostrar el laberinto
def mostrar_laberinto(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

    for fila in matriz:
        print("".join(fila))  # Imprime cada fila del laberinto

# Función principal del juego
def main_loop(laberinto_mapa, posicion_inicial, posicion_final):
    laberinto_matriz = crear_laberinto(laberinto_mapa)
    px, py = posicion_inicial

    laberinto_matriz[py][px] = 'P'

    while (px, py) != posicion_final:
        mostrar_laberinto(laberinto_matriz)
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

    mostrar_laberinto(laberinto_matriz)

    if (px, py) == posicion_final:
        print("\n¡Felicidades! Has escapado del laberinto SNAKE.\n")

# Coordenadas iniciales y finales
posicion_inicial = (0, 0)
posicion_final = (len(laberinto.split('\n')[0]) - 1, len(laberinto.split('\n')) - 1)
        
# Iniciar el juego
main_loop(laberinto, posicion_inicial, posicion_final)
