from math import log10
def is_palindrome(n):
    # easier to read than obfuscated algorithms for integers, and still relatively fast
    return str(n) == str(n)[::-1]

# by good i mean 2 3-digit numbers
def has_good_factors(n):
    for i in range(100, 1000):
        if n%i == 0:
            k = log10(n/i)
            if k < 3 and k > 2:
                return True
    return False

for num in range(999*999, 1, -1):
    if is_palindrome(num) and has_good_factors(num):
        print(num)
        break
