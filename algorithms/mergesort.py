import time
def mergeSortHelper(alist, comparaciones, intercambios):
    if len(alist)>1:
        middle = len(alist)//2
        left=alist[:middle]
        rigth=alist[middle:]
        mergeSortHelper(left, comparaciones, intercambios)
        mergeSortHelper(rigth, comparaciones, intercambios)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(rigth):
            comparaciones+=1
            if left[i]<rigth[j]:
                intercambios+=1
                alist[k] = left[i]
                i+=1
            else:
                intercambios+=1
                alist[k] = rigth[j]
                j+=1
            k+=1
        while i < len(left):
            comparaciones+=1
            intercambios+=1
            alist[k] = left[i]
            i+=1
            k+=1
        while j<len(rigth):
            comparaciones+=1
            intercambios+=1
            alist[k] = rigth[j]
            j+=1
            k+=1
    return [alist,comparaciones,intercambios]


def mergeSort(alist):
    start=time.time()
    comparaciones=0
    intercambios=0
    values=mergeSortHelper(alist,comparaciones,intercambios)
    end= time.time()
    elapsedtime= end-start
    print("Tiempo: ",elapsedtime)
    print("Comparaciones",values[1])
    print("Intercambios",values[2])
    return values[0]