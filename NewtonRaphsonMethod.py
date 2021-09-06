x=1
for i in range(100):
    xnew = x - ((x**3) + x - 1)/(3 * (x**2) + 1)
    if abs(xnew - x) < 0.001: break
    x= xnew
print("The root is %f at %d iterations."%(xnew, i))


