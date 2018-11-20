from algorithms.utilidades import imprimeTablaComplejidad
import time
from math import log2

intercambios=0
comparaciones=0

def swap(i,j,lista):                    
    lista[i], lista[j] = lista[j], lista[i] 

def heapify(final,i,lista):
    global comparaciones
    global intercambios   
    l=2 * i + 1  
    r=2 * (i + 1)   
    maximo=i   
    if l < final and lista[i] < lista[l]:
        comparaciones+=1   
        maximo = l   
    if r < final and lista[maximo] < lista[r]:
        comparaciones+=1   
        maximo = r   
    if maximo != i:   
        swap(i, maximo,lista)
        intercambios+=1
        heapify(final, maximo,lista)   

def heap_sort(lista):
    iter=0
    global intercambios     
    final = len(lista)   
    inicio  = final // 2 - 1 
    for i in range(inicio , -1, -1):   
        heapify(final, i,lista)   
    for i in range(final-1, 0, -1):
        iter+=1   
        swap(i, 0,lista)
        intercambios+=1   
        heapify(i, 0,lista)
        print('ITERACIÓN '+str(iter)+':'+str(lista))

def heapSort(alist):
    n=len(alist)
    nlogn=n*log2(n)
    global comparaciones
    global intercambios
    start=time.clock()
    heap_sort(alist)
    end=time.clock()
    realizadas=[comparaciones,intercambios]

    comparaciones = [f"n*log(n)={round(nlogn,2)}",
                     f"n*log(n) = {round(nlogn,2)}"]
    desplazamientos = [
        f"n*log(n)={round(nlogn,2)}", f"de 0 a n*log(n) = {[0,round(nlogn,2)]}"]

    imprimeTablaComplejidad(
        "Intercambios", comparaciones, desplazamientos, realizadas, end-start)

    return alist
