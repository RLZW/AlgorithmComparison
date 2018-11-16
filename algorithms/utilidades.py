from tabulate import tabulate


def imprimeTablaComplejidad(tipo, comparaciones, intercambios, realizadas, tiempo):
    """Crea la tabla de complejidades recibiendo 3 listas con 2 elementos  y un parametro de tiempo."""

    headers = [" ", "COMPARACIONES", tipo]
    data1 = [("Notación O", comparaciones[0], intercambios[0]),
             ("Complejidad", comparaciones[1], intercambios[1]),
             ]

    data2 = [("Realizadas", realizadas[0], realizadas[1])]
    print(tabulate(data1, headers=headers, tablefmt="fancy_grid"))
    print(tabulate(data2, headers=headers, tablefmt="fancy_grid"))

    print(f'El tiempo de ejecución fue el siguiente: {tiempo}')

