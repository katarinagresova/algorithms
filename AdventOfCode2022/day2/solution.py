input_file = 'input.txt'

code1 = {
    "A Y": 8,
    "A X": 4,
    "A Z": 3,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 2,
    "C X": 7,
    "C Z": 6
}

code2 = {
    "A Y": 3+1,
    "A X": 0+3,
    "A Z": 6+2,
    "B Y": 3+2,
    "B X": 0+1,
    "B Z": 6+3,
    "C Y": 3+3,
    "C X": 0+2,
    "C Z": 6+1
}

def run_part1():

    with open(input_file) as f:
        score = sum([code1[line.rstrip()] for line in f])
    print('Total score is is:', score)

def run_part2():

    with open(input_file) as f:
        score = sum([code2[line.rstrip()] for line in f])
    print('Total score is is:', score)


if __name__ == '__main__':
    run_part1()
    run_part2()