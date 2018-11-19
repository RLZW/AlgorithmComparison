from algorithms.utilidades import imprimeTablaComplejidad

import time
intercambios = 0
particiones = 0
index = 0
iteracion = 0


def quickSort(alist):
    start = time.clock()

    quickSortHelper(alist, 0, len(alist)-1)

    end = time.clock()
    times = end - start

    print(particiones)
    print(times)


def quickSortHelper(alist, first, last):
    global iteracion
    iteracion += 1
    print(f"ITERACIÓN {iteracion}: {alist}")
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    global particiones
    particiones += 1

    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
