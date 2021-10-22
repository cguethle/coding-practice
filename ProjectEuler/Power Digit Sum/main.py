import scipy.special
from datetime import datetime


def get_sum_via_comb(n):
    total = 0
    for x in range(n+1):
        total += scipy.special.comb(n, x, exact=True)

    summation = 0
    for c in str(total):
        summation += int(c)

    return summation


def get_sum_via_math(n):
    a = str(2 ** n)
    b = 0
    for i in range(0, len(a)):
        b += int(a[i])
    return b


n = 2000

start = datetime.now()
print(get_sum_via_comb(n))
print(datetime.now() - start)

start = datetime.now()
print(get_sum_via_math(n))
print(datetime.now() - start)
