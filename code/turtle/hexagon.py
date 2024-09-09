''' turtle hexagon

'''
import turtle


def main():
    ''' main function'''
    my_shape = turtle.Turtle()
    my_other = turtle.Turtle()
    num_sides = 6
    side_length = 70
    angle = 360 / num_sides
    for i in range(num_sides):
        my_shape.forward(side_length)
        my_shape.right(angle)
        my_other.forward(side_length)
        my_other.left(angle)
    turtle.done()


if __name__ == '__main__':
    main()
