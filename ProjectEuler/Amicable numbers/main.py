import math
from datetime import datetime


sums = {}


def _get_proper_divisors_sum(n):
    # could likely be better as we are brute force calculating all
    # proper divisors for numbers we have already solved.
    # maybe hash table of entries?
    # magical math formula or trick? 5 cool ways to solve this that will shock you? :)
    divisors = [x for x in range(1, (n // 2) + 1) if n % x == 0]
    return sum(divisors)


def _get_proper_divisors_sum_better(n):
    # don't process to n // 2.
    # process to sqrt(n) and then store both the found value and its complement.
    divisors = [1]
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            divisors.extend([x, n // x])
    return sum(divisors)


def get_proper_divisors_sum(n, fnc):

    results = []

    for i in range(1, n + 1):
        proper_divisors_sum = fnc(i)
        if proper_divisors_sum:
            sums[i] = proper_divisors_sum
    for i in range(1, n + 1):
        try:
            pair = sums[i]
            if sums[pair] == i and pair != i:
                results.append((pair, i))
        except KeyError:
            # entry doesn't exist... move on.
            pass
    # print(results)

    final_sum = sum(i0 + i1 for i0, i1 in results) // 2  # // 2 to remove duplicates we didn't filter...

    print(final_sum)


if __name__ == "__main__":
    limit = 20000

    start = datetime.now()
    get_proper_divisors_sum(limit, _get_proper_divisors_sum)
    print(f"_get_proper_divisors_sum took {datetime.now() - start} seconds.")
    start = datetime.now()
    get_proper_divisors_sum(limit, _get_proper_divisors_sum_better)
    print(f"_get_proper_divisors_sum_better took {datetime.now() - start} seconds.")


""" output....

115818
_get_proper_divisors_sum took 0:00:06.066648 seconds.
115818
_get_proper_divisors_sum_better took 0:00:00.108539 seconds.

"""


