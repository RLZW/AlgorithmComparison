from algorithms.utilidades import imprimeTablaComplejidad


import time


def bubbleSortHelp(alist, comparaciones, intercambios):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if alist[j] > alist[j+1]:
                intercambios += 1
                alist[j], alist[j+1] = alist[j+1], alist[j]
        print("ITERACIÓN", i+1, " :", alist)
    return [alist, comparaciones, intercambios]


def bubbleSort(alist):
    comparaciones = 0
    intercambios = 0
    start = time.clock()
    valor = bubbleSortHelp(alist, comparaciones, intercambios)
    end = time.clock()

    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    realizadas = [valor[1], valor[2]]

    imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparaciones, desplazamientos, realizadas, end-start)

    return valor[1]
