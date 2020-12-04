import re

INPUT_FILE = 'input.txt'


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


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

        # do not forget to add last passport
        passports.append(passport)

    return passports


def contains_passport_all_fields(passport):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    return set(mandatory_fields) <= set(passport.keys())


def is_byr_valid(byr):
    if not is_int(byr):
        return False

    byr = int(byr)
    return 1920 <= byr <= 2002


def is_iyr_valid(iyr):
    if not is_int(iyr):
        return False

    iyr = int(iyr)
    return 2010 <= iyr <= 2020


def is_eyr_valid(eyr):
    if not is_int(eyr):
        return False

    eyr = int(eyr)
    return 2020 <= eyr <= 2030


def is_hgt_valid(hgt):
    number = hgt[:-2]
    unit = hgt[-2:]

    if not is_int(number):
        return False

    number = int(number)

    if unit == 'cm':
        return 150 <= number <= 193
    elif unit == 'in':
        return 59 <= number <= 76
    else:
        return False


def is_hcl_valid(hcl):

    if len(hcl) != 7:
        return False

    regex = r'#[0-9,a-f]{6}'
    m = re.search(regex, hcl)
    return m is not None


def is_ecl_valid(ecl):
    valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_values


def is_pid_valid(pid):

    if len(pid) != 9:
        return False

    regex = r'[0-9]{9}'
    m = re.search(regex, pid)
    return m is not None


def are_all_field_valid(passport):
    if not is_byr_valid(passport['byr']):
        return False

    if not is_iyr_valid(passport['iyr']):
        return False

    if not is_eyr_valid(passport['eyr']):
        return False

    if not is_hgt_valid(passport['hgt']):
        return False

    if not is_hcl_valid(passport['hcl']):
        return False

    if not is_ecl_valid(passport['ecl']):
        return False

    if not is_pid_valid(passport['pid']):
        return False

    return True


def is_passport_valid(passport):

    if not contains_passport_all_fields(passport):
        return False

    if not are_all_field_valid(passport):
        return False

    return True


def run_part1():
    passports = parse_input()
    counter = 0
    for passport in passports:
        if contains_passport_all_fields(passport):
            counter += 1

    print("Number of passports containing all fields:", counter)


def run_part2():
    passports = parse_input()
    counter = 0
    for passport in passports:
        if is_passport_valid(passport):
            counter += 1

    print("Number of valid passports:", counter)


if __name__ == '__main__':
    run_part1()
    run_part2()
