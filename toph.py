mod=1000000007
T=int(input())
while(T):
    u=int(input())
    v=int(input())
    l=log2(u)+1
    r=log2(v)+1
    ck=u
    ans=0
    q=r-1
    while(q):
        n1=(2**l)
        n2=n1-ck
        ck=n1
        d=(n2*i)%mod
        ans=(ans%mod+d%mod)%mod
        q=q-1
        l=l+1
    n3 = v - ck + 1
    d1 = (n3* r) % mod
    ans = (ans % mod + 1 % mod) % mod
    print(ans)
    T=T-1
