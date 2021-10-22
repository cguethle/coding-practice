from ProjectEuler.utils import get_primes, get_prime_factors, get_num_divisors


primes = get_primes(65500)

current_triangle = 2
prev = 1
number_of_divisors = 0
while True:
    prev = prev + current_triangle
    facts = get_prime_factors(prev, primes)
    num_divisors = get_num_divisors(facts)
    number_of_divisors = number_of_divisors if number_of_divisors > num_divisors else num_divisors
    if num_divisors > 499:
        print(prev)
        break
    current_triangle += 1
