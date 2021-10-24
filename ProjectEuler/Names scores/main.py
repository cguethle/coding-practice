import string


letter_scores = {s: i + 1 for i, s in enumerate(string.ascii_lowercase)}


def get_base_name_score(name_to_score):
    return sum([letter_scores[letter.lower()] for letter in name_to_score])


if __name__ == "__main__":
    total_score = 0
    with open("names.txt", "r") as names_file:
        names = names_file.read()
        names = names.split(",")
        for i in range(len(names)):
            names[i] = names[i].replace('"', "")
        names.sort()

        for i, name in enumerate(names):
            total_score += get_base_name_score(name) * (i + 1)

    print(total_score)
