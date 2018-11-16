from algorithms.utilidades import imprimeTablaComplejidad

import time


def mergeSortHelper(alist, comparaciones, intercambios):
    contador = 0
    if len(alist) > 1:
        middle = len(alist) // 2
        left = alist[:middle]
        rigth = alist[middle:]
        mergeSortHelper(left, comparaciones, intercambios)
        mergeSortHelper(rigth, comparaciones, intercambios)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                comparaciones += 1
                alist[k] = left[i]
                i += 1
            else:
                comparaciones += 1
                alist[k] = rigth[j]
                j += 1
            k += 1
        while i < len(left):
            intercambios += 1
            alist[k] = left[i]
            i += 1
            k += 1
            contador += 1
            print("Iteración", contador, ":", alist)
        while j < len(rigth):
            intercambios += 1
            alist[k] = rigth[j]
            j += 1
            k += 1
            contador += 1
            print("Iteración", contador, ":", alist)
    return [alist, comparaciones, intercambios]


def mergeSort(alist):
    start = time.time()
    comparaciones = 0
    intercambios = 0
    values = mergeSortHelper(alist, comparaciones, intercambios)
    end = time.time()
    elapsedtime = end - start

    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    realizadas = [values[1], values[2]]
    imprimeTablaComplejidad(
        "INTERCAMBIOS", comparaciones, desplazamientos, realizadas, elapsedtime)


    return values
