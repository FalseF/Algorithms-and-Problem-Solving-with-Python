a=[]
sum=1
for i in range (1,1000):
    sum=sum*i
    a.append(int(sum))
N=100
while(N):
    print(a[N])
    N=N-1
