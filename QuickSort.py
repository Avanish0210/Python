def partition(arr , st , end):
    n= int(len(arr))
    pivot = arr[end]
    indx = st-1
    for i in range(st , end):
        #all smaller values on left
        if arr[i]<=pivot:
            indx = indx + 1
            #swap between i and indx
            arr[i],arr[indx]=arr[indx],arr[i]
    #now pivot value to be at right position
    indx = indx + 1
    arr[indx],arr[end]=arr[end],arr[indx]
    #now all smaller values on left and greater on right
    return indx

def QS(arr , st , end):
    if st<end:
        piviotindx = partition(arr , st , end)
        QS(arr,st,piviotindx-1)
        QS(arr,piviotindx+1,end)

arr = [5,2,6,4,1,3]
QS(arr,0,len(arr)-1)
for i in arr:
    print(i,end=' ')
