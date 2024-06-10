import re


def post_cleaning(number, hundreds_upper):
    number = number.replace("un-cent", "cent")
    number = number.replace("un-mille", "mille")
    number = re.sub(r'-+', '-', number)
    number = number.strip('-')
    number = re.sub('-un$', "-et-un", number) if not number.endswith("quatre-vingt-un") and not any(
        number.endswith(ending + "-un") for ending in [i[1] for i in hundreds_upper]) else number
    number = re.sub(r'quatre-vingt$', "quatre-vingts", number)
    if any(number.endswith(ending) and not number.endswith("un-" + ending) for ending in
           [i[1] for i in hundreds_upper]) and number not in ["cent", "mille"]:
        number += "s"
    return number


def file_to_list(file_path, tuple=False, encoding="UTF-8"):
    lines = []

    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            stripped_line = line.strip()
            if tuple:
                key, value = stripped_line.split(":", 1)
                lines.append((eval(key), value))
            else:
                lines.append(stripped_line)

    return lines


def list_to_file(file_path, output):
    with open(file_path, "w", encoding="utf-8") as file:
        for word in output:
            file.write(word + "\n")


def detect_initial_position(number, HundredsUpper, maximum_length):
    if len(str(number)) < 3:
        return len(HundredsUpper) - 1
    for pos, value in enumerate(HundredsUpper):
        if ((number // 10 ** value[0]) != 0) and (len(str(number)) < maximum_length):
            return pos
    return None
