import turtle

def draw_square(turtle_arg):
    for i in range(0,4):
        turtle_arg.forward(100)
        turtle_arg.right(90)

def draw_triangle(turtle_arg):
    for i in range(0,3):
        turtle_arg.forward(100)
        turtle_arg.right(120)

def create_turtle(shape, color, speed):
    instance = turtle.Turtle()
    instance.shape(shape)
    instance.color(color)
    instance.speed(speed)
    return instance

def main():
    screen = turtle.Screen()
    screen.bgcolor("red")
    turtle_square = create_turtle(shape="turtle", color="yellow", speed=3)
    draw_square(turtle_square)
    turtle_circle = create_turtle(shape="arrow", color="blue", speed=3)
    turtle_circle.circle(100)
    turtle_triangle = create_turtle(shape="classic", color="green", speed=3)
    draw_triangle(turtle_triangle)
    screen.exitonclick()
    
    
main()

