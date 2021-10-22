import math
from datetime import datetime

s = datetime.now()
N = 2000000
primes = [0, 0]+[1]*(N-2)
checking = 2

while checking <= N - 1:
    if primes[checking] and N // checking >= 2:
        upperbound = (N-1) // checking
        for k in range(2, upperbound + 1):
            primes[checking * k] = 0
    checking += 1

prime_values = [idx for idx, value in enumerate(primes) if value]
summation = sum(prime_values)
# print(prime_values)
# print(sum(prime_values))
print(f"found {summation} in {datetime.now() - s}s")

s = datetime.now()


def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


summation = 0
for x in range(2, 2000000):
    if is_prime(x):
        summation += x
# print(f"hard summation: {summation}")
print(f"found {summation} in {datetime.now() - s}s")
