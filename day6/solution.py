INPUT_FILE = 'input.txt'


def read_lines():
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()

    return lines


def run_part1():

    group_answers = ''
    sum_of_counts = 0

    for line in read_lines():
        # groups are separated by empty lines
        if line == '\n':
            sum_of_counts += len(set(group_answers))
            group_answers = ''
        # just concatenate all answers from one group together
        else:
            group_answers += line.strip()

    # do not forget to count the last one
    sum_of_counts += len(set(group_answers))

    print("Sum of counts:", sum_of_counts)


def count_everyone_answered_yes(values, group_size):
    count = 0
    for value in values:
        if value == group_size:
            count += 1

    return count


def run_part2():
    group_answers_by_char = {}
    group_size = 0
    sum_of_counts = 0

    for line in read_lines():
        # groups are separated by empty lines
        if line == '\n':
            sum_of_counts += count_everyone_answered_yes(group_answers_by_char.values(), group_size)
            group_answers_by_char = {}
            group_size = 0
        else:
            # count answers for each option
            for char in line.strip():
                if char in group_answers_by_char:
                    group_answers_by_char[char] += 1
                else:
                    group_answers_by_char[char] = 1
            group_size += 1

    # do not forget to count the last one
    sum_of_counts += count_everyone_answered_yes(group_answers_by_char.values(), group_size)

    print("Sum of counts:", sum_of_counts)


if __name__ == '__main__':
    run_part1()
    run_part2()