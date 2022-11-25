# Fibonacci series
import math
a = input("Enter any number or numbers: ").split(",")
b = []
for i in a:
    b.append(int(i))
b = sorted(b)
def isperfectsquare(c):
    d = int(math.sqrt(c))
    return d*d == c
def isfibo(n):
    return isperfectsquare(5*n*n+4) or isperfectsquare(5*n*n-4)
for i in b:
    if isfibo(i) == True:
        print(i, "is in Fibonacci series")
    else:
        print(i, "is not in Fibonacci series")
