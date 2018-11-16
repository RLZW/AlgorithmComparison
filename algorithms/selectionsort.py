from algorithms.utilidades import imprimeTablaComplejidad

import time


def selectionSortHelp(alist, comparaciones, intercambios):
    for i in range(len(alist)-1):
        comparaciones += 1
        mini = i
        for j in range(i+1, len(alist)):
            if(alist[mini] > alist[j]):
                intercambios += 1
                mini = j
        alist[i], alist[mini] = alist[mini], alist[i]
        print("ITERACION", i+1, " :", alist)
    return [alist, comparaciones, intercambios]


def selectionSort(alist):
    comparaciones = 0
    intercambios = 0
    start = time.clock()
    valor = selectionSortHelp(alist, comparaciones, intercambios)
    end = time.clock()

    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    realizadas = [valor[1], valor[2]]

    imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparaciones, desplazamientos, realizadas, end-start)

    return valor[1]
