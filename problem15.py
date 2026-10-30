from math import factorial

def perms(n):
    return factorial(n) / (factorial(n//2)*factorial(n//2))

print(perms(40))
