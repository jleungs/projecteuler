from math import sqrt

for a in range(1,1000):
    for b in range(1,1000):
        if (a + b + sqrt(a**2 + b**2)) == 1000:
            c = int(sqrt(a**2 + b**2))
            print(a,b,c,a*b*c)

