input_file = 'input.txt'

def run_part1():
    max_sum = 0

    with open(input_file) as f:
        sum = 0
        for line in f:
            if line.rstrip() == '':
                max_sum = max(max_sum, sum)
                sum = 0
            else:
                sum += int(line.rstrip())
    max_sum = max(max_sum, sum)
    print('Max number of calories carried by single Elf is:', max_sum)

def run_part2():
    sums = []
    with open(input_file) as f:
        sum = 0
        for line in f:
            if line.rstrip() == '':
                sums.append(sum)
                sum = 0
            else:
                sum += int(line.rstrip())
    sums.append(sum)
    sums = sorted(sums)
    print('Max number of calories carried by top thee Elf are:', sums[-1] + sums[-2] + sums[-3])

if __name__ == '__main__':
    run_part1()
    run_part2()