import time
def insertionSortHelper(alist,intercambios,comparaciones):
    for index in range(1, len(alist)):
        comparaciones+=1
        currentvalue = alist[index]
        position = index
        while (position > 0) and (alist[position - 1] > currentvalue):
            intercambios+=1
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue
    return [alist,intercambios,comparaciones]


def insertionSort(alist):
    start = time.time()
    compaciones = 0
    intecambios = 0
    values = insertionSortHelper(alist,intecambios,compaciones)
    end = time.time()
    elapsedtime = end-start
    print("Tiempo: ",elapsedtime)
    print("comparaciones: ",values[2])
    print("intercambios: ",values[1])
    return values