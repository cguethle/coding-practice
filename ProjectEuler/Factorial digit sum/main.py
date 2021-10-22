from math import factorial


def get_factoral_digit_sum(n):
    """
    Find the sum as described below.

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    """
    fact = str(factorial(n))
    return sum([int(digit) for digit in fact])


if __name__ == "__main__":
    print(get_factoral_digit_sum(100))
