import time
def selectionSortHelp(alist, comparaciones, intercambios):
    for i in range(len(alist)):
        mini = i
        comparaciones+=1
        for j in range(i+1, len(alist)):
            if(alist[mini] > alist[j]):
                intercambios+=1
                mini = j
        alist[i], alist[mini] = alist[mini], alist[i]
    return [alist, comparaciones, intercambios]

def selectionSort(alist):
    comparaciones = 0
    intercambios = 0
    start = time.time()
    valor = selectionSortHelp(alist, comparaciones, intercambios)
    end = time.time()
    print("Tiempo", end-start )
    print("Comparaciones", valor[1])
    print("Intercambios", valor[2])
    return valor[1]