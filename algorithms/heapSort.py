from algorithms.utilidades import imprimeTablaComplejidad
import time


intercambios = 0
comparaciones = 0


def heapify(arreglo, n, i):
    global comparaciones
    global intercambios
    mas_grande = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arreglo[i] < arreglo[l]:
        comparaciones += 1
        mas_grande = l
    if r < n and arreglo[mas_grande] < arreglo[r]:
        comparaciones += 1
        mas_grande = r
    if mas_grande != i:
        arreglo[i], arreglo[mas_grande] = arreglo[mas_grande], arreglo[i]
        intercambios += 1
        heapify(arreglo, i, 0)


def sort(arreglo):
    iter = 0
    global intercambios
    n = len(arreglo)
    for i in range(n, -1, -1):
        heapify(arreglo, n, i)

    for i in range(n-1, 0, -1):
        iter += 1
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
        intercambios += 1
        heapify(arreglo, i, 0)
        print('ITERACION '+str(iter)+':'+str(arreglo))


def heapSort(alist):
    global comparaciones
    global intercambios
    start = time.clock()
    sort(alist)
    end = time.clock()

    realizadas = [comparaciones, intercambios]

    comparaciones = [f"n²={len(alist)**2}",
                     f"((n-1)n)/2 = {((len(alist)-1)*len(alist))/2}"]
    desplazamientos = [
        f"n²={len(alist)**2}", f"de 0 a ((n-1)n)/2 = {[0,((len(alist)-1)*len(alist))/2]}"]

    imprimeTablaComplejidad(
        "Intercambios", comparaciones, desplazamientos, realizadas, end-start)

    return alist

#print(heapSort([ 12, 11, 13, 5, 6, 7]))
