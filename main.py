import random
import socket
from algorithms.quicksort import quickSort

# ¡LEER!
# Al añadir un nuevo algoritmo favor de meterlo en la carpeta algorithms y asignarle su respectiva referencia
# En la lista de algoritmos y su condición en la la función correrAlgoritmo
# El algoritmo de ordenamiento tiene que recibir una lista y regresarla ordenada,
# También tiene que imprimir lo siguiente:
# Número de comparaciones
# Número de intercambios
# Númeor de desplazamientos
# Tiempo

# TODO: Faltan todos los algoritmos de ordenamiento, con sus debidas comparaciones, itercambios, desplazamientos y tiempo



algoritmos = ["QuickSort"]


def correrAlgoritmo(listaNumeros):
    """Recibe la lista y pregunta el número del algoritmo que desea ser corrido y lo corre"""

    print("Los algoritmos que puedes utilizar, son los siguientes: ")
    for i in range(len(algoritmos)):
        print(f'{i+1} - {algoritmos[i]}')

    respuesta = int(input(
        "Ingresa el número del algoritmo con el que quieres ordenar tus números: "))

    if(respuesta == 1):
        quickSort(listaNumeros)


def pedirCantidadDeNumeros():
    """Pide la cantidad de números a ser generado"""
    cantidad = int(
        input("-Ingrese la cantidad de números que desea ser generado: "))
    return cantidad


def _generarNumeros(cantidad):
    """Genera una lista con números random recibiendo la cantidad de elementos a ser generados"""
    my_randoms = [random.randrange(-1001, 1001, 1) for _ in range(cantidad)]
    return my_randoms


def ingresaGenera():
    """Regresa True si se desean ingresar y False si se desean generar aleatoriamente"""
    res = input(
        "Deseas ingresar numeros[X] o generarlos aleatoriamente[A]: ").lower()
    if res == "x":
        return True
    if res == "a":
        return False
    else:
        ingresaGenera()
    return res


def ingresaNumeros():
    """Pide números separados por espacio y regresa una lista de los mismos"""
    numeros = input("Ingresa tus números separados por espacio: ")
    numeros = numeros.split(" ")
    numeros = list(map(int, numeros))
    return numeros


def generaAleatorios():
    """Genera todo el ciclo de pedir y regresar números aleatorios, regresa la lista"""
    cantidad = pedirCantidadDeNumeros()
    numeros = _generarNumeros(cantidad)
    return numeros


def menu():
    res = ingresaGenera()

    if(res):
        listaNumeros = ingresaNumeros()
    else:
        listaNumeros = generaAleatorios()

    print("La lista de números es la siguiente:")
    print(listaNumeros)

    correrAlgoritmo(listaNumeros)

    print(listaNumeros)


def main():
    menu()


if __name__ == '__main__':
    main()
