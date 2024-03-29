import time
from algorithms.utilidades import imprimeTablaComplejidad
from math import log2
intercambios = 0
comparaciones = 0
index = 0


def mergeSortHelper(alist):
    global intercambios
    global comparaciones
    global index

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
            index+=1
            #print('ITERACIÓN ', index, ':', alist)
            if left[i] < rigth[j]:
                intercambios+=1
                comparaciones += 1
                alist[k] = left[i]
                i += 1
            else:
                intercambios+=1
                alist[k] = rigth[j]
                j += 1
            k += 1
        while i < len(left):
            intercambios += 1
            alist[k] = left[i]
            i += 1
            k += 1
            print('ITERACIÓN ', index, ':', alist)
            index += 1
        while j < len(rigth):
            index+=1
            intercambios += 1
            alist[k] = rigth[j]
            j += 1
            k += 1
            print('ITERACIÓN ', index, ':', alist)
            index += 1
        print('ITERACIÓN ', index, ':', alist)
        index += 1
    return [alist, comparaciones, intercambios]


def mergeSort(alist):
    n=len(alist)
    nlogn=n*log2(n)
    start = time.time()
    global comparaciones
    global intercambios
    values = mergeSortHelper(alist)
    end = time.time()
    elapsedtime = end - start
    comparaciones = [f"n*log(n)={round(nlogn,2)}",
                     f"n*log(n) = {round(nlogn,2)}"]
    desplazamientos = [
        f"n*log(n)={round(nlogn,2)}", f"de 0 a n*log(n) =  {[0,round(nlogn,0)]}"]

    realizadas = [values[2], values[1]]

    imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparaciones, desplazamientos, realizadas, elapsedtime)
    return values
