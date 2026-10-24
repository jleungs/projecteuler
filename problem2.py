a, b = 1, 2
sums = 0
while b < 4_000_000:
    if b % 2 == 0:
        sums += b
    a, b = b, a+b
print(sums)
