import time
def selectionSortHelp(alist, comparaciones, intercambios):
    for index in range(len(alist)-1,0,-1):
        comparaciones+=1
        positionOfMax=0
        for location in range(1,index+1):
            intercambios+=1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[index]
        alist[index] = alist[positionOfMax]
        alist[positionOfMax] = temp
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