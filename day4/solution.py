INPUT_FILE = 'input.txt'


def parse_input():

    passports = []
    passport = {}

    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():

            # end of passport record
            if line == '\n':
                passports.append(passport)
                passport = {}

            else:
                fields = line.strip().split(' ')
                for field in fields:
                    separator_index = field.index(':')
                    key = field[:separator_index]
                    value = field[separator_index + 1:]
                    passport[key] = value

    return passports


def is_valid_passport(passport):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    return set(mandatory_fields) <= set(passport.keys())


def run_part1():
    passports = parse_input()
    counter = 0
    for passport in passports:
        if is_valid_passport(passport):
            counter += 1

    print("Number of valid passports:", counter)

if __name__ == '__main__':
    run_part1()
