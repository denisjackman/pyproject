'''
    Turtle test
    from : https://michael0x2a.com/blog/turtle-examples
'''
import turtle


def main():
    ''' main '''
    turtle.circle(50)
    turtle.shape("turtle")
    turtle.color("Red")

    turtle.circle(100)
    turtle.color("Blue")
    turtle.circle(150)
    turtle.color("Green")

    turtle.circle(200)
    turtle.color("Black")
    turtle.shape("arrow")

    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.mainloop()
    turtle.color('red')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(70)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()


if __name__ == '__main__':
    main()
