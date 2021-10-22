import math

nth_prime = 10001
primes_found = 0
highest_prime = 0
current_value = 2


def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


while primes_found < nth_prime:
    if is_prime(current_value):
        primes_found += 1
        highest_prime = current_value
    current_value += 1

print(highest_prime)
