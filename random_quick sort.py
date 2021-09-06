import random
def quicksort(A,low,high):
    if (low<high):
        pivot=randompartition(A,low,high)
        quicksort(A,low,pivot)
        quicksort(A,pivot+1,high)
def randompartition(A,low,high):
    pivot=random.randrange(low,high)
    A[low],A[pivot] = A[pivot],A[low]
    return partition(A,low,high)
def partition(A,low,high):
    pivot=low
    i=low-1
    j=high+1
    while True:
        while True:
            i=i+1
            if A[i]>=A[pivot]:
                break
        while True:
            j=j-1
            if A[j]<=A[pivot]:
                break
        if i>=j:
            return j
        A[i],A[j]=A[j],A[i]
A = [10, 7, 8, 9, 1, 5]
quicksort(A,0,len(A)-1)
for i in range (len(A)):
    print(A[i])