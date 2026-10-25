def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def get_prime(n):
    p = 2
    while n > 0:
        if is_prime(p):
            n -= 1
        p += 1

    return p-1

print(get_prime(10_001))
