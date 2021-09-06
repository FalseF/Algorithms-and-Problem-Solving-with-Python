def BIGMOD(base,power,mod):
    if power==1:
        return base%mod
    elif power==0:
        return 1
    elif power%2==0:
        p=BIGMOD(base,power/2,mod)
        return (p*p)%mod
    elif power%2!=0:
        p=base%mod
        q=BIGMOD(base,power-1,mod)
        return  (p*q)%mod
base=int(input())
power=int(input())
mod=int(input())
print(BIGMOD(base,power,mod))