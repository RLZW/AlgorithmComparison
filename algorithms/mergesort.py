import time
from algorithms.utilidades import imprimeTablaComplejidad
intercambios=0
comparaciones=0


def mergeSortHelper(alist):
    global intercambios
    global comparaciones
    if len(alist) > 1:
        middle = len(alist) // 2
        left = alist[:middle]
        rigth = alist[middle:]
        mergeSortHelper(left)
        mergeSortHelper(rigth)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(rigth):
            print (alist)
            if left[i] < rigth[j]:
                comparaciones += 1
                alist[k] = left[i]
                i += 1
            else:
                comparaciones+=1
                alist[k] = rigth[j]
                j += 1
            k += 1
        while i < len(left):
            intercambios+=1
            alist[k] = left[i]
            i += 1
            k += 1
            print(alist)
        while j < len(rigth):
            intercambios+=1
            alist[k] = rigth[j]
            j += 1
            k += 1
            print(alist)
    return [alist, comparaciones,intercambios]


def mergeSort(alist):
    start = time.time()
    global comparaciones
    global intercambios
    values = mergeSortHelper(alist)
    end = time.time()
    elapsedtime = end - start
    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    realizadas = [values[2], values[1]]

    imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparaciones, desplazamientos, realizadas, elapsedtime)
    return values
