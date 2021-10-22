import math


def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


def is_palindrome(number):
    number_str = str(number)
    for i in range((len(number_str) // 2) + 1):
        if number_str[i] != number_str[-(i + 1)]:
            return False
    return True


candidate = 999*999
print(f"largest_possible = {candidate}")


while True:
    if is_palindrome(candidate) and not is_prime(candidate):
        print(f"finding factors for {candidate}")
        factor = 999
        while candidate % factor != 0 and candidate // factor < 1000:
            print(f"remainder: {candidate % factor}, other: {candidate // factor}")
            factor -= 1
        if candidate // factor < 1000:
            print(f"found match: {factor} * {candidate // factor}")
            break
    candidate -= 1
    if candidate == 0:
        break

print(candidate)
