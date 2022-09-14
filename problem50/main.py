from math import sqrt
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def generate_primes_below_n(n):
    sieve=[ True ]* ( n//2 )
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i//2]:
            sieve[ i*i //2 :: i ] = [False] * (( n-i*i-1) //(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime_triv(n):
    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            return False
    return True

n = 4_000 # sum of 4_000 primes is above 1e6
nums = generate_primes_below_n(n)
s = sum(nums)
limit = 1e6
while True:
    n -= 1
    s = sum(nums[:n]) - 10
    if is_prime_triv(s):
        if s < limit:
            break

print(s)
