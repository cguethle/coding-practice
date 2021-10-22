
class Path:
    def __init__(self, sum, sequence=None):
        self.sum = sum
        self.sequence = sequence or []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"sum: {self.sum} ; sequence: {self.sequence}"


def get_max_path_sum(numbers):
    for x in range(len(numbers)-2, -1, -1):
        line = numbers[x]
        prev_line = numbers[x+1]
        for y in range(len(prev_line) - 1):
            current_value = line[y]
            if isinstance(prev_line[y], int):
                chose = max(prev_line[y], prev_line[y + 1])
                line[y] = Path(chose + line[y], sequence=[chose, line[y]])
            else:
                path_to_promote = prev_line[y] if (prev_line[y].sum + current_value) > \
                                                  (prev_line[y+1].sum + current_value) \
                    else prev_line[y+1]
                line[y] = Path(
                    path_to_promote.sum + current_value,
                    path_to_promote.sequence.copy()
                )
                line[y].sequence.append(current_value)

    return numbers[0][0]


if __name__ == "__main__":
    number_list = []
    with open('input.txt', 'r') as input_file:
        text = "default"
        while text:
            text = input_file.readline()
            if text:
                number_list.append(
                    [int(num) for num in text.split(" ")]
                )

    path = get_max_path_sum(number_list)

    print(f"path sum: {path.sum}")
    print(f"path order: {path.sequence}")
