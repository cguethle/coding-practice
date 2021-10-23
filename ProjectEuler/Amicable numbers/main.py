sums = {}


def get_proper_divisors_sum(n):
    # could likely be better as we are brute force calculating all
    # proper divisors for numbers we have already solved.
    # maybe hash table of entries?
    # magical math formula or trick? 5 cool ways to solve this that will shock you? :)
    divisors = [x for x in range(1, (n // 2) + 1) if n % x == 0]
    return sum(divisors)


if __name__ == "__main__":
    limit = 10000
    results = []

    for i in range(1, limit+1):
        proper_divisors_sum = get_proper_divisors_sum(i)
        if proper_divisors_sum:
            sums[i] = proper_divisors_sum
    for i in range(1, limit+1):
        try:
            pair = sums[i]
            if sums[pair] == i and pair != i:
                results.append((pair, i))
        except KeyError:
            # entry doesn't exist... move on.
            pass

    final_sum = sum(i0 + i1 for i0, i1 in results) // 2     # // 2 to remove duplicates we didn't filter...

    print(final_sum)
