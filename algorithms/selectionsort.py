import time
def selectionSortHelp(alist, comparaciones, intercambios, desplazamientos):
    for i in range(len(alist)-1):
        comparaciones+=1
        mini = i
        for j in range(i+1, len(alist)):
            desplazamientos+=1
            if(alist[mini] > alist[j]):
                intercambios+=1
                mini = j
        alist[i], alist[mini] = alist[mini], alist[i]
    return [alist, comparaciones, intercambios, desplazamientos]

def selectionSort(alist):
    comparaciones = 0
    intercambios = 0
    desplazamientos = 0
    start = time.time()
    valor = selectionSortHelp(alist, comparaciones, intercambios, desplazamientos)
    end = time.time()
    print("Tiempo", end-start )
    print("Comparaciones", valor[1])
    print("Intercambios", valor[2])
    print("Desplazamientos", valor[3])
    return valor[1]