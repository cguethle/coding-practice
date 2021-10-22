from ProjectEuler.utils import print_matrix, create_dyn_grid

import scipy.special
import datetime


def get_total_via_dynamic_programming(size):
    grid = create_dyn_grid(size, size)

    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            grid[r][c] = grid[r-1][c] + grid[r][c-1]

    return grid[size][size]


def get_total_via_combinatorics(size):
    return scipy.special.comb(size*2, size, exact=True)


size_to_test = 2000

start = datetime.datetime.now()
print(get_total_via_dynamic_programming(size_to_test))
print(f"dynamic_programming time in seconds: {datetime.datetime.now() - start}")


start = datetime.datetime.now()
print("%i" % get_total_via_combinatorics(size_to_test))
print(f"combinatorics time in seconds: {datetime.datetime.now() - start}")