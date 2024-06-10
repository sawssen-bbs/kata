from context import NumberToWordsContext
from tools import file_to_list, detect_initial_position, post_cleaning, list_to_file


def main():
    # read configurations
    units = file_to_list("configurations/units.txt")
    tens = file_to_list("configurations/tens.txt")
    hundredsUpper = file_to_list("configurations/hundredsUpper.txt", tuple=True)

    input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199,
             200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111,
             12345, 123456, 654321, 999999, "o"]

    maximum_length = len(str(10 ** hundredsUpper[0][0])) + 3
    output = []

    for number in input:
        result = ""
        if type(number) != int:
            output.append("only numbers are accepted")
        else:
            number_to_words = NumberToWordsContext(units, tens)
            pos = detect_initial_position(number, hundredsUpper, maximum_length)
            result = number_to_words.transform(number, pos, hundredsUpper, maximum_length)
            output.append(post_cleaning(result, hundredsUpper))

    print(output)

    list_to_file("output.txt", output)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
