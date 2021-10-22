sum = 2
n2, n1, c = 1, 2, 3
while c <= 4000000:
    print(c, sum)
    if c % 2 == 0:
        sum += c
    n2, n1 = n1, c
    c = n1 + n2

print(sum)

