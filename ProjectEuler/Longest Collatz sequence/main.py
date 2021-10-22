import time

hash_cache = {
    1: 1,
    2: 2
}


def collatz_length(n):
    # print(f"collatz_length for {n}")
    # time.sleep(1)

    next_value = n
    length = 0
    while next_value != 1:
        # print(f"processing next_value = {next_value}")
        # time.sleep(1)
        if next_value in hash_cache.keys():
            # print(f"cache hit!  {next_value}")
            hash_cache[n] = length + hash_cache[next_value]
            return hash_cache[n]

        if next_value % 2 == 0:
            next_value = int(next_value // 2)
        else:
            next_value = 3 * next_value + 1
        length += 1

    # print(f"returning {length} for collatz_length({n})")
    hash_cache[n] = length
    return length


# print(f"collatz_length(5) = {collatz_length(5)}")
# print(hash_cache)
# print(f"collatz_length(13) = {collatz_length(13)}")
# print(hash_cache)




maximum = 0
maximum_value = 0
for x in range(1, 1000000):
    candidate = collatz_length(x)
    if maximum < candidate:
        maximum = candidate
        maximum_value = x

print(maximum)
print(maximum_value)
print(max(hash_cache.values()))












#
# def collatz_length_simple(n):
#     next_value = n
#     length = 1
#     while next_value != 1:
#         if next_value % 2 == 0:
#             next_value /= 2
#         else:
#             next_value = 3 * next_value + 1
#         length += 1
#     return length
#

