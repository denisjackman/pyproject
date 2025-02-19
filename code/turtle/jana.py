''' turtle hexagon

'''
import turtle


def main():
    ''' main function'''
    my_shape = turtle.Turtle()
    my_other = turtle.Turtle()
    my_screen = turtle.Screen()
    my_screen.bgcolor("black")
    my_shape.pencolor("red")
    my_other.pencolor("green")
    num_sides = 6
    side_length = 70
    angle = 360 / num_sides
    for loop in range(100):
        my_shape.pendown()
        my_other.pendown()

        for _ in range(num_sides):
            my_shape.forward(side_length)
            my_shape.right(angle)
            my_other.forward(side_length)
            my_other.left(angle)
            my_other.hideturtle()
            my_shape.hideturtle()
        my_shape.penup()
        my_other.penup()
        my_other.left(side_length/2)
        my_shape.left(side_length/2)
        loop += 1

    turtle.done()


if __name__ == '__main__':
    main()
