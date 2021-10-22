numbers = []

with open('input.txt', 'r') as input_file:
    text = "default"
    while text:
        text = input_file.readline().strip()
        if text:
            numbers.append(text)

total_sum = sum([int(n) for n in numbers])
print(str(total_sum)[:10])
