from time import sleep
import timeit


# def magic_square(dataset):
#     n = len(dataset)
#     magic_sum = int(n * (n**2 + 1) / 2)
#     print(magic_sum)
#     operations = []
#     for r in dataset:
#         row_sum = sum(r)
#         print(row_sum - magic_sum)


if __name__ == "__main__":



    # dataset = [
    #     [4, 8, 2],
    #     [4, 5, 7],
    #     [6, 1, 6]
    # ]
    #
    # # magic_square(dataset)
    #
    # N = 3
    # magic_square = []*N
    # print(magic_square)
    # n = 1
    # i, j = 0, n // 2
    # while n <= N ** 2:
    #     magic_square[i][j] = n
    #     n += 1
    #     newi, newj = (i - 1) % N, (j + 1) % N
    #     if magic_square[newi][newj]:
    #         i += 1
    #     else:
    #         i, j = newi, newj
    #
    # print(magic_square)