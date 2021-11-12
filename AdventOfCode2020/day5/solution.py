INPUT_FILE = 'input.txt'


def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


def read_seats():
    with open(INPUT_FILE, 'r') as f:
        ids = f.read().splitlines()

    return ids


def decode_seat_location(seat):
    num_row_chars = 7
    num_columns_chars = 3

    row_binary = ''
    for row_char in seat[:num_row_chars]:
        if row_char == 'F':
            row_binary += '0'
        elif row_char == 'B':
            row_binary += '1'
        else:
            print('Unknown character:', row_char)
            exit(1)

    column_binary = ''
    for column_char in seat[num_row_chars:]:
        if column_char == 'L':
            column_binary += '0'
        elif column_char == 'R':
            column_binary += '1'
        else:
            print('Unknown character:', column_char)
            exit(1)

    return binary_to_decimal(row_binary), binary_to_decimal(column_binary)


def run_part1():
    seats = read_seats()
    biggest_id = 0

    for seat in seats:
        row, column = decode_seat_location(seat)
        seat_id = row * 8 + column
        if seat_id > biggest_id:
            biggest_id = seat_id

    print('Biggest id:', biggest_id)


def run_part2():
    seat_list = set([row * 8 + column for  row in range(127) for column in range(7)])
    seats = read_seats()
    for seat in seats:
        row, column = decode_seat_location(seat)
        seat_id = row * 8 + column
        if seat_id in seat_list:
            seat_list.remove(seat_id)

    print('Possible seats:', seat_list)
    print('Look through them and find some left alone in the middle.')


if __name__ == '__main__':
    run_part1()
    run_part2()
