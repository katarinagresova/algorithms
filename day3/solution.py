INPUT_FILE = 'input.txt'
TREE_SYMBOL = '#'
SLOPE_RIGHT = 3
SLOPE_DOWN = 1


def read_file():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    return lines


def count_trees():
    area = read_file()

    x = 0
    y = 0
    counter = 0
    height = len(area)
    width = len(area[0])

    while y < height:
        if y == 322:
            print("hey")
        if area[y][x % width] == TREE_SYMBOL:
            counter += 1
        x += SLOPE_RIGHT
        y += SLOPE_DOWN

    return counter


def run_part1():
    count = count_trees()
    print('Encountered trees:', count)


if __name__ == '__main__':
    run_part1()