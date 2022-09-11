def print_fibonacci(n):
    sum = 0
    a = 0
    b = 1
    c = 1
    while c < n :
        a = b
        b = c
        c = a+b
        if c % 2 == 0:
            sum += c
    return sum

sum = print_fibonacci(4_000_000)
print(sum)
