def largest_palindrome(n):
    largest = 0
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            res = i*j
            if str(res) == str(res)[::-1]:
                if res > largest:
                    largest = res
    return largest

print(largest_palindrome(999))
