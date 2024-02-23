from readchar import readkey, key

print("Presiona cualquier tecla (Flecha arriba para salir):")

while True:
    k = readkey()
    
    if k == key.UP :  # Verifica si se presionó la tecla de flecha hacia arriba (↑)
        print("Tecla de flecha hacia arriba presionada. Saliendo del programa.")
        break
    else:
        print(f"Tecla presionada: {k}")