''' fizzbuzz program '''


def main():
    ''' fizzbuzz program'''
    for item in range(1, 101):
        if item % 3 == 0 and item % 5 == 0:
            print(f"{item} fizzbuzz")
        elif item % 3 == 0:
            print(f"{item} fizz")
        elif item % 5 == 0:
            print(f"{item} buzz")
        else:
            print(f"{item}")


if __name__ == "__main__":
    main()
