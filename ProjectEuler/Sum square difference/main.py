
first_x_numbers = 100
print(
    sum(x for x in range(first_x_numbers + 1))**2 -
    sum([x**2 for x in range(first_x_numbers + 1)])
)
