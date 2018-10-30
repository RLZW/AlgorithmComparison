import random


def pedirCantidadDeNumeros():
    cantidad = int(
        input("-Ingrese la cantidad de números que desea ser generado: "))
    return cantidad


def generarNumeros(cantidad):
    my_randoms = [random.randrange(-1001, 1001, 1) for _ in range(cantidad)]
    return my_randoms


def main():
    cantidad = pedirCantidadDeNumeros()
    numeros = generarNumeros(cantidad)
    print('La lista de números es la siguiente:')
    print(numeros)


if __name__ == '__main__':
    main()
