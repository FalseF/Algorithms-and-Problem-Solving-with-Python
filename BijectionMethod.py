def BisectionMethod(x):
    return ((x**3)-9*x+1)
a=2
b=4
for i in range(1,20):
    x0 =(a+b)/2
    print(x0)
    print()
    fx0=BisectionMethod(x0)
    fa=BisectionMethod(a)
    fb = BisectionMethod(b)
    if fa*fx0<0:
        b=x0
    else:
        a=x0