import re

INPUT_FILE = 'input.txt'


def parse_line(passw_line):
    regex = r'([1-9][0-9]*)-([1-9][0-9]*)\s([a-z]):\s([a-z]*)'
    m = re.findall(regex, passw_line)[0]
    return int(m[0]), int(m[1]), m[2], m[3]


def is_passw_valid_part1(passw_line):
    lower_limit, upper_limit, character, passw = parse_line(passw_line)

    regex = r'' + character
    m = re.findall(regex, passw)

    return lower_limit <= len(m) <= upper_limit


def is_passw_valid_part2(passw_line):
    first_position, second_position, character, passw = parse_line(passw_line)

    return (passw[first_position - 1] == character and passw[second_position - 1] != character) \
        or (passw[first_position - 1] != character and passw[second_position - 1] == character)


def count_valid_passw(part1=True):
    counter = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            if part1:
                if is_passw_valid_part1(line):
                    counter += 1
            else:
                if is_passw_valid_part2(line):
                    counter += 1

    return counter


def run_part1():
    count = count_valid_passw(part1=True)
    print("Number of valid passwords:", count)


def run_part2():
    count = count_valid_passw(part1=False)
    print("Number of valid passwords:", count)


if __name__ == '__main__':
    run_part1()
    run_part2()
