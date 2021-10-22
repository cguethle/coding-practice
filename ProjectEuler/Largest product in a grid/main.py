from math import prod


grid = []


def print_matrix(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f"{array[i][j]}\t", end="")
        print("")
    print("-----")


with open('input.txt', 'r') as input_file:
    text = "default"
    while text:
        text = input_file.readline()
        # print(text)
        if text:
            grid.append(
                [int(num) for num in text.split(" ")]
            )


print_matrix(grid)

max_product_candidate = None
max_product = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        products = []
        print(f"starting at ({r}, {c})")
        right = c + 3 < len(grid[r])
        left = c - 3 > -1
        up = r - 3 > -1
        down = r + 3 < len(grid)
        if up:
            products.append(prod([
                    grid[r][c], grid[r-1][c], grid[r-2][c], grid[r-3][c]
            ]))
            if right:
                products.append(prod([
                    grid[r][c], grid[r - 1][c + 1], grid[r - 2][c + 2], grid[r - 3][c + 3]
                ]))
            if left:
                products.append(prod([
                    grid[r][c], grid[r - 1][c - 1], grid[r - 2][c - 2], grid[r - 3][c - 3]
                ]))
        if down:
            products.append(prod([
                grid[r][c], grid[r + 1][c], grid[r + 2][c], grid[r + 3][c]
            ]))
            if right:
                products.append(prod([
                    grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2], grid[r + 3][c + 3]
                ]))
            if left:
                products.append(prod([
                    grid[r][c], grid[r + 1][c - 1], grid[r + 2][c - 2], grid[r + 3][c - 3]
                ]))
        if left:
            products.append(prod([
                grid[r][c], grid[r][c - 1], grid[r][c - 2], grid[r][c - 3]
            ]))
        if right:
            products.append(prod([
                grid[r][c], grid[r][c + 1], grid[r][c + 2], grid[r][c + 3]
            ]))
        if products:
            max_product = max(
                max_product,
                max(products)
            )
print(max_product)
