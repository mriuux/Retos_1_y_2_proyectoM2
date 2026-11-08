# Proyecto Módulo 2 - Fundamentos de Python

## Descripción

Este proyecto corresponde al producto terminado del Módulo 2 de Fundamentos de Python.

El programa integra los dos retos realizados durante el módulo:

1. **Validación de palabras:** solicita una palabra al usuario y verifica que contenga solamente letras y que tenga una longitud entre 4 y 8 caracteres.
2. **Ubicación de un punto:** solicita las coordenadas "x" y "y" y determina en qué cuadrante se encuentra el punto.

Los dos retos se encuentran integrados en un solo programa mediante un menú principal.

## Funcionalidades

### 1. Validación de palabra

El programa solicita al usuario una palabra y realiza diferentes validaciones:

- Comprueba que solamente contenga letras.
- Comprueba que tenga como mínimo 4 caracteres.
- Comprueba que no tenga más de 8 caracteres.
- Guarda todos los intentos realizados por el usuario en una lista.

La lista utilizada es:

"palabras_intentadas = []"

Esto permite almacenar los diferentes registros de palabras ingresadas durante la sesión.

### 2. Ubicación del punto

El segundo reto solicita las coordenadas "x" y "y" al usuario.

Las coordenadas se convierten de texto a números mediante "float()". También se utiliza manejo de excepciones para evitar que el programa se detenga cuando el usuario introduce un valor que no puede convertirse a número.

El programa identifica el cuadrante utilizando las condiciones de los signos de las coordenadas.

Para almacenar los nombres de los cuadrantes se utiliza una tupla:

"cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")"

Posteriormente, se utiliza un índice para acceder al cuadrante correspondiente.

## Estructuras utilizadas

Durante el desarrollo del proyecto se utilizaron diferentes estructuras y elementos de Python:

- **Variables:** para almacenar valores como las coordenadas "x", "y" y los números ingresados.
- **Listas:** para almacenar las palabras que el usuario intentó ingresar.
- **Tuplas:** para almacenar los nombres de los cuadrantes.
- **Condicionales "if", "elif" y "else":** para realizar validaciones y determinar el cuadrante.
- **Ciclo "while":** para repetir las solicitudes hasta que el usuario introduzca información válida.
- **Ciclo "for":** para recorrer la lista de palabras intentadas.
- **Funciones:** para organizar el programa en diferentes bloques de trabajo.
- **Excepciones "try" y "except":** para controlar errores al convertir las coordenadas.
- **Casting con "float()":** para convertir las coordenadas ingresadas como texto a números decimales.

## Manejo de errores

El programa utilza "try" y "except" para controlar los errores que pueden ocurrir cuando el usuario introduce información incorrecta.

Por ejemplo, si se escribe texto en lugar de un número para una coordenada, el programa muestra un mensaje de error y vuelve a solicitar el dato sin detener su ejecución.

También se valida que las coordenadas sean diferentes de cero y que sean números finitos.

## Organización del programa

El programa está dividido en diferentes funciones para facilitar su lectura y mantenimiento:

- "comparar_longitud()"
- "solicitar_numero()"
- "evaluar_cuadrante()"
- "mostrar_palabras_intentadas()"
- "mostrar_menu()"

El menú principal permite seleccionar el reto que se desea ejecutar o consultar las palabras ingresadas durante la sesión.

## Reflexión

Durante el desarrollo de los retos pude comprender mejor cómo las estructuras de control ayudan a organizar la lógica de un programa.

Los condicionales "if", "elif" y "else" fueron importantes para tomar decisiones dependiendo de los datos ingresados por el usuario. En el reto de los cuadrantes, por ejemplo, permitieron determinar la ubicación del punto dependiendo de los valores positivos o negativos de las coordenadas.

Los ciclos "while" también mejoraron la lógica del programa porque permiten repetir una solicitud cuando el usuario introduce un dato incorrecto, evitando que el programa termine de manera inesperada.

Además, el uso de funciones permitió dividir el problema en partes más pequeñas y fáciles de comprender. La incorporación de listas y tuplas también ayudó a organizar mejor los datos y a evitar repetir información dentro del código.

En general, estos elementos hicieron que el programa fuera más ordenado, fácil de leer y más resistente a errores. El proyecto me permitió comprender que las estructuras de control no solamente sirven para ejecutar instrucciones, sino que también ayudan a construir una lógica más clara y organizada.

## Conclusión

La integración de los dos retos permitió aplicar los conocimientos adquiridos durante el módulo en un solo programa. El uso de funciones, estructuras de control, colecciones, casting y manejo de excepciones permitió mejorar la organización y funcionamiento del código.

Este proyecto representa la consolidación de los conocimientos trabajados en los retos de validación de palabras y ubicación de puntos mediante cuadrantes.
