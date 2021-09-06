def FalsePosition(f,x1,x2,tol=1.0*10**-6,maxfpos=20):
    xh = 0
    fpos = 0
    if f(x1) * f(x2) < 0:
        for fpos in range(1,maxfpos+1):
            xh = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol: break
            elif f(x1) * f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print("No root exists within the given interval.")
    return xh,fpos
y = lambda x: x**3  + x - 1
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
r,n = FalsePosition(y,x1,x2)
print("The root = %f at %d false positions."%(r,n))



