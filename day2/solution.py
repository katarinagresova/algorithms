import re

INPUT_FILE = 'input.txt'


def parse_line(passw_line):
    regex = r'([1-9][0-9]*)-([1-9][0-9]*)\s([a-z]):\s([a-z]*)'
    m = re.findall(regex, passw_line)[0]
    return int(m[0]), int(m[1]), m[2], m[3]


def is_passw_valid(passw_line):
    lower_limit, upper_limit, character, passw = parse_line(passw_line)

    regex = r'' + character
    m = re.findall(regex, passw)

    return lower_limit <= len(m) <= upper_limit


def count_valid_passw():
    counter = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            if is_passw_valid(line):
                counter += 1

    return counter


def run_part1():
    count = count_valid_passw()
    print("Number of valid passwords:", count)


if __name__ == '__main__':
    run_part1()