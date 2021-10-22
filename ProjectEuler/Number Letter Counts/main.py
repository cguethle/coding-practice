
HUNDRED = "hundred"
THOUSAND = "thousand"
AND = "and"

number_to_string_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def get_string_repr(value: int) -> str:
    """
    Returns a string representation (English) of the integer value.
    """
    # base... take care of all of the fixed cases.
    if value in number_to_string_map.keys():
        return number_to_string_map[value]

    return_string = ""

    # process ones
    ones = value % 10

    if ones > 0:
        return_string = number_to_string_map[ones]

    # process tens
    tens = value % 100
    if tens in number_to_string_map.keys():
        return_string = number_to_string_map[tens]
    else:
        value -= ones
        tens = value % 100
        if tens > 0:
            return_string = f"{number_to_string_map[tens]}{'-' + return_string if return_string else ''}"

    value -= tens

    # process hundreds
    hundreds = value % 1000
    value -= hundreds

    if hundreds:
        return_string = f"{number_to_string_map[hundreds // 100]} {HUNDRED}" \
                        f"{f' {AND} ' + return_string if return_string else ''}"

    if value:
        # 1 thousand!
        return_string = f"{number_to_string_map[1]} {THOUSAND}"

    return return_string


def get_letter_count(string_to_count: str) -> int:
    """
    Gets the count of the letters in the string excluding spaces and hyphens.
    """
    string_to_count = string_to_count.replace(" ", "")
    string_to_count = string_to_count.replace("-", "")
    return len(string_to_count)


if __name__ == "__main__":
    input_value = 1000
    total = 0
    for x in range(1, input_value+1):
        str_to_add = get_string_repr(x)
        letter_cnt = get_letter_count(str_to_add)
        total += letter_cnt
    print(total)
