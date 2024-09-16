''' quiz 82
what is the answer to the following code

1) str int
2) str int
3) str str
4) int str

The answer is 4)

the explanation is
var intially is an integer type.
when 'hello' is assigned to it, it becomes a string (str type)
'''


def main():
    ''' main function'''
    var = 10
    print(type(var))
    var = 'hello'
    print(type(var))


if __name__ == '__main__':
    main()
