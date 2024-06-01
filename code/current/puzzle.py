''' puzzle play script '''


def puzzle_foo(a, b, *args, **kwargs):
    ''' foo '''
    return a + b + sum(args) + sum(kwargs.values())


def main():
    ''' main '''
    print("[=] Puzzle Play Start")
    print(f"[-] foo: {puzzle_foo(1, 2, 3, 4, x=5, y=6)}")
    print("[=] Puzzle Play Done.")


if __name__ == "__main__":
    main()
