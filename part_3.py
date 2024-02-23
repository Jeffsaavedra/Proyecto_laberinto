from readchar import readkey
import os
number = 0

def borrar_consola():
    os.system('cls' if os.name=='nt' else 'clear')

while number <= 50:
    borrar_consola()
    print("Presiona 'n' para aumentar el número. Presiona cualquier otra tecla para salir.")
    print(f"Número: {number}")
    llave = readkey()
        
    if llave == 'n':
        number += 1
    else:
        break