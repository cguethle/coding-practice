from time import sleep
import timeit


def binary_search_iterative(data, n, first=False, last=False):
    """
    search array "data" for value "n". returning the index of the found element, or -1 if not found.
    :param data: data values
    :type data: list
    :param n: value to search for
    :type n: int
    """
    if first and last:
        raise ValueError("Can't search both first and last.")

    begin, end = 0, len(data) - 1
    result = -1

    while begin <= end:
        mid = int(begin + (end - begin) / 2)    # avoid overflow
        candidate = data[mid]
        if candidate == n:
            if not (first or last):
                return mid
            else:
                result = mid
                if first:
                    end = mid - 1
                else:
                    begin = mid + 1
        elif n > candidate:
            # go up...
            begin = mid + 1
        elif n < candidate:
            # go down...
            end = mid - 1

    return result


def binary_occurrences_iterative(data, n):
    """
    search array "data" for value "n". returning the index of the found element, or -1 if not found.
    :param data: data values
    :type data: list
    :param n: value to search for
    :type n: int
    """
    left_found, right_found = False, False
    first_discovered_index = -1
    begin, end = 0, len(data) - 1
    result = 0

    while begin <= end:
        mid = int(begin + (end - begin) / 2)    # avoid overflow
        candidate = data[mid]
        if candidate == n:
            first_discovered_index = mid
            result += 1
            break
        elif n > candidate:
            # go up...
            begin = mid + 1
        elif n < candidate:
            # go down...
            end = mid - 1

    while 

    return result


def binary_search_recursive(data, n, start=None, end=None):
    """
    Do it recursively....
    """
    result = -1
    start, end = (0, len(data) - 1) if start is None or end is None \
        else (start, end)
    mid = int(start + (end - start) / 2)

    candidate = data[mid]
    if candidate == n:
        return mid
    elif start == end:
        return result
    else:
        return \
            binary_search_recursive(data, n, start, mid) if candidate > n \
            else binary_search_recursive(data, n, mid+1, end)


def number_of_occurrences(data, n, start=None, end=None):
    start, end = (0, len(data) - 1) if start is None or end is None \
        else (start, end)
    mid = int(start + (end - start) / 2)

    candidate = data[mid]
    if candidate == n:
        if start == end:
            return 1
        else:
            return \
                number_of_occurrences(data, n, start, mid-1) + \
                number_of_occurrences(data, n, mid + 1, end) + \
                1
    elif start == end:
        return 0
    else:
        return number_of_occurrences(data, n, start, mid-1) if candidate > n \
            else number_of_occurrences(data, n, mid + 1, end)


def run_test(data, test_case, expected, func):
    index = func(data, test_case)
    if index == -1:
        print(f"{test_case} not found in the data.")
    else:
        print(f"Found {test_case} at index {index}.")

    assert expected == index, f"Should have been at index {expected}, found at {index} instead."


if __name__ == "__main__":
    dataset = [5, 12, 34, 56, 89, 204, 443, 595, 929]

    test_values = [
        (595, 7),
        (5, 0),
        (929, 8),
        (89, 4),
        (25, -1)
    ]

    print("Testing using binary_search_iterative...")
    for v, expected in test_values:
        run_test(dataset, v, expected, binary_search_iterative)

    print("Testing using binary_search_recursive...")
    for v, expected in test_values:
        run_test(dataset, v, expected, binary_search_recursive)

    dataset_2 = [2, 4, 10, 10, 10, 18, 20]

    assert binary_search_iterative(dataset_2, 10, first=True) == 2, "First 10 should be at index 2."
    assert binary_search_iterative(dataset_2, 10, last=True) == 4, "Last 10 should be at index 4."

    print("Testing number_of_occurrences...")

    assert number_of_occurrences(dataset_2, 10) == 3, "There should be 3 occurrences of 10."
    assert number_of_occurrences(dataset_2, 6) == 0, "There should be 0 occurrences of 6."

    assert binary_search_iterative(dataset_2, 10, last=True) - binary_search_iterative(dataset_2, 10, first=True) + 1 == 3

    big_dataset = [10]*90000000

    print(timeit.timeit(lambda: binary_search_iterative(big_dataset, 10, last=True) -
                                binary_search_iterative(big_dataset, 10, first=True) + 1
                        , number=5))

    print(f"binary_occurrences_iterative - {binary_occurrences_iterative(dataset_2, 10)}")

