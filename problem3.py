from math import prod

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def gen_prime(n):
    for i in range(n):
        if is_prime(i):
            yield i

number = 600851475143
primes = []
for p in gen_prime(number // 2):
    if number % p == 0:
        primes.append(p)
    if prod(primes) == number:
        break

print(primes)

