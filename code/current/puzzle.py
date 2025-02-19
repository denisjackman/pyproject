''' puzzle play script '''


def puzzle_foo(a, b, *args, **kwargs):
    ''' foo '''
    return a + b + sum(args) + sum(kwargs.values())


def puzzle_func(a=1, b=2, c=3):
    ''' func '''
    return a * b * c


def main():
    ''' main '''
    print("[=] Puzzle Play Start")
    print(f"[-] func: {puzzle_func(5, c=4)}")
    print(f"[-] foo: {puzzle_foo(1, 2, 3, 4, x=5, y=6)}")
    print("[=] Puzzle Play Done.")


if __name__ == "__main__":
    main()
