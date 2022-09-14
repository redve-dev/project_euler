def my_sum(n):
    s = 0
    for i in range(1, n+1):
        s += pow(i, i, int( 1e10 ))
    return s % int(1e10)

print(my_sum(1000))
