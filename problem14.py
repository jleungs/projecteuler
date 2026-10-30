def collatz(n):
    terms = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1
        if n in cdict:
            return terms + cdict[n]
        terms += 1

    return terms

cdict = {}
for i in range(1, 1_000_000):
    cdict[i] = collatz(i)

print(max(cdict, key=cdict.get))
