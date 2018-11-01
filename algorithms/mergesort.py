def mergeSort(alist):
    if len(alist)>1:
        middle = len(alist)//2
        left=alist[:middle]
        rigth=alist[middle:]
        mergeSort(left)
        mergeSort(rigth)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(rigth):
            if left[i]<rigth[j]:
                alist[k] =left[i]
                i+=1
            else:
                alist[k]= rigth[j]
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
    return alist