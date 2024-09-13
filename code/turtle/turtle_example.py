''' simple turtle example
    links
        https://sqlpad.io/tutorial/beginners-guide-python-turtle/
    '''
import turtle


def main():
    ''' main function '''
    # Set up the screen
    wn = turtle.Screen()
    wn.title("My First Turtle Program")
    wn.bgcolor("lightblue")

    # Create a turtle
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("green")

    # Move the turtle
    my_turtle.forward(100)  # Move the turtle forward by 100 units
    my_turtle.left(90)      # Turn the turtle left by 90 degrees
    my_turtle.forward(50)   # Move the turtle forward by 50 units

    # Close the window on a click
    wn.exitonclick()


def draw_fractal(length):
    ''' draw fractal '''
    if length > 5:
        my_turtle = turtle.Turtle()
        my_turtle.forward(length)
        my_turtle.right(90)
        draw_fractal(length - 5)  # Recursive call


if __name__ == '__main__':
    main()
    # draw_fractal(100)
