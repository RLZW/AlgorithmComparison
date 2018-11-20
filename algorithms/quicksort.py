from algorithms.utilidades import imprimeTablaComplejidad

import time
desplazamientos = 0
comparaciones = 0
iteraciones = 0


def quickSort(alist):
    start = time.time()
    quickSortHelper(alist, 0, len(alist))
    end = time.time()

    elapsedtime = end - start

    comparacionesteor = [f"n²={len(alist)**2}",
                         f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientosteor = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    realizadas = [comparaciones, desplazamientos]
    imprimeTablaComplejidad(
        "DESPLAZAMIENTOS", comparacionesteor, desplazamientosteor, realizadas, elapsedtime)
    return alist


def quickSortHelper(lista, low, high):
    global comparaciones, desplazamientos, iteraciones
    iteraciones += 1    
    print('ITERACIÓN ', iteraciones, ':', lista)
    if (low >= high):
        return


    pivote = lista[high - 1]
 
    limite = low

    for i in range(low, high):
        comparaciones += 1

        if (lista[i] <= pivote):
            desplazamientos += 1
            temp = lista[limite]
            lista[limite] = lista[i]
            lista[i] = temp
            limite = limite + 1
            if limite >= high:
                break

    quickSortHelper(lista, low, limite - 1)
    quickSortHelper(lista, limite, high)
