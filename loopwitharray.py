
a=[]
n=int(input())
for i in range(0,n):
    b=input()
    a.append(int(b))
sort(a)
for i in range(n):
    print(a[i],end=' ')