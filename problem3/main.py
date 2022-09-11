def biggest_prime_factor(n):
    divisor = 2
    max_div = 2
    while n > 1:
        while n%divisor == 0:
            max_div = divisor
            n /= divisor
        divisor += 1
    return max_div

num = 600_851_475_143
print(biggest_prime_factor(num))
