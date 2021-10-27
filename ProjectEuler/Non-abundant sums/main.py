import math


def _get_proper_divisors(n):
    divisors = [1]
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            divisors.append(x)
            if n // x != x:
                divisors.append(n // x)
    return divisors


def _get_proper_divisors_sum(n):
    result = sum(_get_proper_divisors(n))
    return result


def _is_abundant(n):
    return _get_proper_divisors_sum(n) > n


def get_abundant_numbers():
    result = []
    for x in range(1, 28124):
        if _is_abundant(x):
            result.append(x)
    return result


"""
Find all positive integers <=28123 that are __not__ the sum of 2 __abundant__ numbers.
"""
if __name__ == "__main__":
    answers = []
    ceiling = 28124

    abundant = get_abundant_numbers()

    abundant_sums = set()
    for i in abundant:
        for j in abundant:
            summ = i + j
            if summ > ceiling:
                break
            abundant_sums.add(summ)

    answers = [x for x in range(1, ceiling + 1) if x not in abundant_sums]

    print(sum(answers))
