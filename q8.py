def print_multplication_table():
    """Function to print a multiplication table 12x12"""
    print('1'.rjust(9), end='')
    for i in range(2, 13):
        print(str(i).rjust(4), end='')
    print()

    line = ':' + 50 * '-'
    print(line.rjust(53))
    for i in range(1, 13):
        print(str(i).rjust(2), end=':\t')
        print(str(i).rjust(5), end='')
        for j in range(2, 13):
            print(str(i * j).rjust(4), end='')
        print()


print_multplication_table()
