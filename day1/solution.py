input_file = 'input.txt'
TARGET_SUM = 2020

with open(input_file) as f:
    numbers = [int(line.rstrip()) for line in f]


def run_part1():
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers) - 1):
            if numbers[i] + numbers[j] == TARGET_SUM:
                print('Numbers are: ', numbers[i], numbers[j])
                print('Multiplication equals:', numbers[i] * numbers[j])
                break


def run_part2():
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers) - 1):
                if numbers[i] + numbers[j] + numbers[k] == TARGET_SUM:
                    print('Numbers are: ', numbers[i], numbers[j], numbers[k])
                    print('Multiplication equals:', numbers[i] * numbers[j] * numbers[k])
                    break


if __name__ == '__main__':
    run_part1()
    run_part2()