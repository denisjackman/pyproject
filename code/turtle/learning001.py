''' a turtle learning session'''
import turtle as t


def main():
    ''' main function '''
    t.bgcolor('black')
    t.pencolor('yellow')
    t.pensize(8)
    t.up()
    t.goto(-200, 0)
    t.down()
    for i in range(5):
        t.forward(400)
        t.right(144)
    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()
