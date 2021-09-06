# Method 1 , My favourite
n=int(input())
array = list(map(int, input().split()))

# method 2
inp=int(input())
for i in range(0,inp):
    array.append(int(input))
for i in  range(len(array)):
    print(array[i],end=" ")