def Fibonacci(n):
    if(n<=1):
        return  n
    else:
        return  Fibonacci(n-1)+Fibonacci(n-2)
n=int (input())
for i in range (0,n):
    print(Fibonacci(i))