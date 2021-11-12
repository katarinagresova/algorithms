INPUT_FILE = 'input.txt'


def parse_rule(rule_line):

    outer_bag = rule_line[:rule_line.index('bags') - 1]
    inner_bags = rule_line[rule_line.index('contain') + 8:].split(',')

    inner_bags = [bag[2:bag.index('bag') - 1].strip() for bag in inner_bags]

    return outer_bag, inner_bags


def read_rules():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    rules = {}
    for line in lines:
        outer_bag, inner_bags = parse_rule(line)
        for inner_bag in inner_bags:
            if inner_bag in rules:
                rules[inner_bag].append(outer_bag)
            else:
                rules[inner_bag] = [outer_bag]

    return rules


def count_outer_bags(rules, bag, counted_bags):

    # end of recursion
    if bag not in rules:
        return set()

    outer = rules[bag]
    counted_bags.update(outer)
    for out in outer:
        counted_bags.update(count_outer_bags(rules, out, counted_bags))

    return counted_bags


if __name__ == '__main__':
    rules = read_rules()
    my_bag = 'shiny gold'
    counted_bags = set()
    print(len(count_outer_bags(rules, my_bag, counted_bags)))
    #print(count_outer_bags.counted_bags)