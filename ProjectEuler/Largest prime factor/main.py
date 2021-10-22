import math


def largest_prime(n):
    div = 2
    while n != 0:
        if n % div != 0:
            div += 1
        else:
            print(f"n = {int(n)}")
            print(f"divides evenly: {div}")
            print(f"is_prime: {is_prime(div)}")
            max_fact = n
            n /= div
            if n == 1:
                print(int(max_fact))
                break


def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


print(largest_prime(8))
# print(largest_prime(600851475143))
