INPUT_FILE = 'input.txt'
TREE_SYMBOL = '#'


def read_file():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    return lines


def count_trees(slope_right, slope_down):
    area = read_file()

    x = 0
    y = 0
    counter = 0
    height = len(area)
    width = len(area[0])

    while y < height:
        if area[y][x % width] == TREE_SYMBOL:
            counter += 1
        x += slope_right
        y += slope_down

    return counter


def run_part1():
    count = count_trees(slope_right=3, slope_down=1)
    print('Encountered trees:', count)


def run_part2():
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    counter = 1

    for slope in slopes:
        counter *= count_trees(slope_right=slope[0], slope_down=slope[1])

    print('Encountered trees on all slopes multiplied:', counter)


if __name__ == '__main__':
    run_part1()
    run_part2()
