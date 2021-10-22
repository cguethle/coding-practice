from collections import defaultdict


def get_primes(n):
    primes = [0, 0]+[1]*(n-2)
    checking = 2

    while checking <= n - 1:
        if primes[checking] and n // checking >= 2:
            upperbound = (n-1) // checking
            for k in range(2, upperbound + 1):
                primes[checking * k] = 0
        checking += 1

    prime_values = [idx for idx, value in enumerate(primes) if value]
    return prime_values


def get_prime_factors(n, prime_list):
    remaining = n
    current_prime_idx = 0
    factors = []
    while remaining != 1:
        if remaining % prime_list[current_prime_idx] == 0:
            remaining /= prime_list[current_prime_idx]
            factors.append(prime_list[current_prime_idx])
        else:
            current_prime_idx += 1
    return factors


def get_num_divisors(prime_factors):
    num_divisors = 1
    prime_counts = defaultdict(int)
    for f in prime_factors:
        prime_counts[f] += 1
    for c in prime_counts:
        num_divisors *= prime_counts[c] + 1
    return num_divisors


def print_matrix(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f"{array[i][j]}\t", end="")
        print("")
    print("-----")


def create_dyn_grid(r, c):
    grid_size = (r, c)

    grid = [[0] * (grid_size[0] + 1) for _ in range(grid_size[1] + 1)]
    for x in range(len(grid)):
        grid[x][0] = 1
    for x in range(len(grid[0])):
        grid[0][x] = 1

    return grid