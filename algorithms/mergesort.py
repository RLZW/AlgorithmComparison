import time
def mergeSortHelper(alist, comparaciones):
    if len(alist)>1:
        middle = len(alist)//2
        left=alist[:middle]
        rigth=alist[middle:]
        mergeSortHelper(left, comparaciones)
        mergeSortHelper(rigth, comparaciones)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(rigth):
            if left[i]<rigth[j]:
                comparaciones += 1
                alist[k] = left[i]
                i+=1
            else:
                comparaciones += 1
                alist[k] = rigth[j]
                j+=1
            k+=1
        while i < len(left):
            alist[k] = left[i]
            i+=1
            k+=1
        while j<len(rigth):
            alist[k] = rigth[j]
            j+=1
            k+=1
    return [alist,comparaciones]


def mergeSort(alist):
    start=time.time()
    comparaciones=0
    values=mergeSortHelper(alist,comparaciones)
    end= time.time()
    elapsedtime= end-start
    print("Tiempo: ",elapsedtime)
    print("Comparaciones",values[1])
    return values[0]