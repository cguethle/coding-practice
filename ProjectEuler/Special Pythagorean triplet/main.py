"""
a*a + b*b = c*c

a+b+c = 1000

a = c*c - b*b  /  a
c = 1000 - a - b

a = (1000 - a - b) * (1000 - a - b) - b * b  /  a
a =



a*a + b*b = 1000 - a - b * 1000 - a - b
"""
from math import prod

for x in range(1, 1001):
    for y in range(x + 1, 1001):
        z = 1000 - x - y
        if x ** 2 + y ** 2 == z ** 2 and x + y + z == 1000:
            print(prod([x, y, z]))
            exit(0)

