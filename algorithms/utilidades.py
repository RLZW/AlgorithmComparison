#lista = ["n^2 = 64","((n-1)n)/2 = 28"]
def imprimeTablaComplejidad(tipo, comparaciones, intercambios, realizadas, tiempo):
    """Crea la tabla de complejidades recibiendo 3 listas con 2 elementos  y un parametro de tiempo."""
    print("-----------------------------------------------------------------------------------")
    print(f"             |       Comparaciones       |       {tipo}")
    print(
        f"Notacion O   |      {comparaciones[0]}      |       {intercambios[0]}")
    print(
        f"Complejidad  |      {comparaciones[1]}      |       {intercambios[1]}")
    print("-----------------------------------------------------------------------------------")
    print(f"Realizadas  |       {realizadas[0]}     |       {realizadas[1]}")
