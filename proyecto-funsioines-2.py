import os
import keyboard


def borrar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_numeros():
    numero = 0
    while numero <= 50:
        borrar_terminal()
        print(f"Número actual: {numero}")
        numero += 1
        keyboard.read_event("n")

mostrar_numeros()

