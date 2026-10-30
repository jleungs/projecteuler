def sums(n):
    return n*(n+1) // 2

def divisors(n):
    divs = set([n])
    i = 1
    while i*i < n:
        if n % i == 0:
            divs.update([i,n//i])
        i += 1
    return divs

i = 1
while len(divisors(sums(i))) < 500:
    i += 1

print(f"{i}: {sums(i)}")
