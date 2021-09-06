def bubble_sort(A):
    for i in range (len(A)):
        for j in range (len(A)-1):
            if(A[j]>A[j+1]):
                A[j+1],A[j]=A[j],A[j+1]
A=[6,1,10,2,4]
bubble_sort(A)
for i in range (len(A)):
    print(A[i])