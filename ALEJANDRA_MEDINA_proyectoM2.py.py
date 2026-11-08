# Reto semanal - Producto Terminado
# Fundamentos de Python
# Proyecto Módulo 2

import math

# ============================================================
# COLECCIONES DEL PROGRAMA
# ============================================================

# Lista que almacena todas las palabras que el usuario intenta ingresar durante la sesión.
palabras_intentadas = []

# Tupla que almacena los nombres de los cuatro cuadrantes.
# Una tupla es una colección ordenada cuyos valores no pueden modificarse durante la ejecución.
cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")

# ============================================================
# RETO 1: VALIDACIÓN DE PALABRAS
# ============================================================

def comparar_longitud():
    """Solicita una palabra al usuario y valida que tenga entre 4 y 8 caracteres y que contenga solamente letras."""

    while True:
        palabra = input("Ingresa una palabra: ")

        # Guarda cada intento en la lista.
        palabras_intentadas.append(palabra)

        # Verifica que solamente se hayan ingresado letras.
        if not palabra.isalpha():
            print("Por favor, ingresa solo letras.")

        # Verifica que la palabra tenga mínimo 4 caracteres.
        elif len(palabra) < 4:
            print("Hacen falta letras. Intenta de nuevo.")

        # Verifica que la palabra no tenga más de 8 caracteres.
        elif len(palabra) > 8:
            print("Sobran letras. Intenta de nuevo.")

        else:
            print("La palabra tiene la longitud correcta.")
            break


# ============================================================
# RETO 2: UBICACIÓN DE UN PUNTO EN UN CUADRANTE
# ============================================================

def solicitar_numero(mensaje):
    """Solicita una coordenada al usuario y valida que sea un número finito diferente de cero."""

    while True:
        try:
            # input() recibe un string y float() realiza el casting de string a número decimal.
            numero = float(input(mensaje))

            # Verifica que el número sea finito.
            if not math.isfinite(numero):
                print("Error: Ingresa un número válido.")

            # Las coordenadas no pueden ser cero.
            elif numero == 0:
                print("Error: la coordenada no puede ser cero.")

            else:
                return numero

        except ValueError:
            # Maneja el error cuando el usuario escribe un valor que no puede convertirse a float.
            print("Error: Ingresa solamente números.")

def evaluar_cuadrante():
    """Solicita las coordenadas X y Y y determina en qué cuadrante se encuentra el punto."""

    x = solicitar_numero("Ingresa la coordenada x: ")
    y = solicitar_numero("Ingresa la coordenada y: ")

    # Se asigna un índice dependiendo de los signos de las coordenadas.
    if x > 0 and y > 0:
        indice = 0

    elif x < 0 and y > 0:
        indice = 1

    elif x < 0 and y < 0:
        indice = 2

    else:
        indice = 3

    # Se utiliza el índice para acceder al nombre correspondiente dentro de la tupla.
    print(f"El punto se encuentra en el {cuadrantes[indice]}.")

# ============================================================
# MOSTRAR PALABRAS INGRESADAS
# ============================================================

def mostrar_palabras_intentadas():
    """Muestra todas las palabras que el usuario intentó ingresar durante la sesión."""

    print("\n--- Palabras intentadas durante la sesión ---")

    if not palabras_intentadas:
        print("No se han ingresado palabras.")

    else:
        for posicion, palabra in enumerate(palabras_intentadas, start=1):
            print(f"Intento {posicion}: {palabra}")

# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    """Muestra el menú principal del programa. Permite seleccionar uno de los dos retos o salir."""

    while True:
        print("\n========================================")
        print("     PROYECTO FINAL - MÓDULO 2")
        print("========================================")
        print("1. Validación de palabra")
        print("2. Ubicación de un punto")
        print("3. Mostrar palabras intentadas")
        print("4. Salir")
        print("========================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n--- RETO 1: VALIDACIÓN DE PALABRA ---")
            comparar_longitud()

        elif opcion == "2":
            print("\n--- RETO 2: UBICACIÓN DEL PUNTO ---")
            evaluar_cuadrante()

        elif opcion == "3":
            mostrar_palabras_intentadas()

        elif opcion == "4":
            print("\nGracias por utilizar el programa.")
            break

        else:
            print("\nOpción no válida. Intenta nuevamente.")

# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

print("========================================")
print("     PROYECTO FINAL - FUNDAMENTOS")
print("========================================")

mostrar_menu()