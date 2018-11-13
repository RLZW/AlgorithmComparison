from utility import _imprimeTablaComplejidad

import time


def insertionSortHelper(alist, intercambios, comparaciones):
    for index in range(1, len(alist)):
        comparaciones += 1
        currentvalue = alist[index]
        position = index
        while (position > 0) and (alist[position - 1] > currentvalue):
            intercambios += 1
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue
    return [alist, intercambios, comparaciones]


def insertionSort(alist):
    start = time.time()
    compaciones = 0
    intecambios = 0
    values = insertionSortHelper(alist, intecambios, compaciones)
    end = time.time()
    elapsedtime = end-start
    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*n)/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*n)/2]}"]

    realizadas = [values[2], values[1]]

    _imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparaciones, desplazamientos, realizadas, elapsedtime)

    return values
