from math import sqrt
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def generate_primes_below_n(n):
    sieve=[ True ]* ( n//2 )
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i//2]:
            sieve[ i*i //2 :: i ] = [False] * (( n-i*i-1) //(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime(n):
    carmichel_nums = {
            341, 561, 1105, 1729, 2465, 2821
            }
    if n in carmichel_nums:
        return False
    return pow(2, n-1, n) == 1

n = 4_000 # sum of 4_000 primes is above 1e6
nums = generate_primes_below_n(n)
s = sum(nums)
limit = 1e6
while True:
    n -= 1
    s = sum(nums[:n]) - 10
    if is_prime(s):
        if s < limit:
            break

print(s)
