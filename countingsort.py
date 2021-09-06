def countingsort(A,mmax):
    C=[0]*(mmax + 1)
    for i in range(len(A)):
        C[A[i]]+= 1
    ndx = 0
    for i in range(len(C)):
        while 0<C[i]:
            A[ndx] = i
            ndx+= 1
            C[i]-=1
A=[8,3,1,10,3]
mmax=10
countingsort(A,mmax)
for i in range(len(A)):
    print(A[i])