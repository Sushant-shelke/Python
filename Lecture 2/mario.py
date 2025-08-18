def main():
    print_row(4)
    print_colmn(3)
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        print()


def print_row(width):
    print("?" * width)


def print_colmn(height):
    print("#\n" * height)


main()
