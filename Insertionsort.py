def insertion_sort(A):
    for i in range (1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key <A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
A=[5,10,2,9,1]
insertion_sort(A)
#for i in range (len(A)):
print(A)