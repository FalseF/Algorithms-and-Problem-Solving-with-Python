cnt=0
def partition(A,low,high):
    global  cnt
    pivot=A[high]
    i=low-1
    for j in range(low,high):
        if(pivot>=A[j]):
            i+=1
            A[i],A[j]=A[j],A[i]
            cnt+=1
    A[i+1],A[high]=A[high],A[i+1]
    cnt+=1
    return  i+1
def quick_sort(A,low,high):
    if(low<high):
        pivot=partition(A,low,high)
        quick_sort(A,low,pivot-1)
        quick_sort(A,pivot+1,high)
A=[10,5,4,1,8]
quick_sort(A,0,len(A)-1)
print(A)
print("Swapping time")
print(cnt)