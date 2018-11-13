import time
def bubbleSortHelp(alist, comparaciones, intercambios):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones+=1
            if alist[j] > alist[j+1] :
                intercambios+=1
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return [alist, comparaciones, intercambios]
def bubbleSort(alist):
    comparaciones = 0
    intercambios = 0
    start = time.clock()
    valor = bubbleSortHelp(alist, comparaciones, intercambios)
    end = time.clock()
    print("Tiempo", end-start )
    print("Comparaciones", valor[1])
    print("Intercambios", valor[2])
    return valor[1]

    