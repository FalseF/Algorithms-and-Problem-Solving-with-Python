def f(x):
    return x**3 + x - 1
#Definition of the derivative of function
def fprime(x):
    return 3*x**2 + 1

#Initialization of variables
epsilon = 0.0001
guess = 1
i = 0

print('Iteration     Guess value of root')

while abs(f(guess)) >= epsilon:
    guess = guess - (f(guess)/fprime(guess))
    i += 1
    print ('    '+ str(i) + '               ' + str(round(guess, 7)))

print('Approximate solution of the root to 2 decimal places is '+str(round(guess,2))+'. It took total of ' + str(i) + ' iterations to converge.')
