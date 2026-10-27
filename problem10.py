def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def gen_prime_below(n):
    p = 1
    while p < n:
        if is_prime(p):
            yield p
        p += 1

print(
    sum(p for p in gen_prime_below(2_000_000))
)
