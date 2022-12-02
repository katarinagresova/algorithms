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
    print('Max number of calories carried by single Elf is:', max_sum)

if __name__ == '__main__':
    run_part1()