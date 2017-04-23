import turtle

bgcolor = "white"

def current_color(level, even_color, odd_color):
    if level % 2 == 0:
        return even_color
    else:
        return odd_color

def draw_triangle(turtle_arg, length, level, even_color, odd_color):
    turtle_arg.color(current_color(level, even_color, odd_color))
    for i in range(0,3):
        if i == 2:
            turtle_arg.pendown()

        turtle_arg.forward(length)
        turtle_arg.right(120)
    if level > 0:
        for i in range(0,3):
            turtle_arg.penup()
            turtle_arg.forward(length/2)
            draw_triangle(turtle_arg, length/2, level-1, even_color, odd_color)
            turtle_arg.penup()
            turtle_arg.forward(length/2)
            turtle_arg.right(120)
    

def create_turtle(shape, color, speed, x=0, y=0):
    instance = turtle.Turtle()
    instance.color(bgcolor)
    instance.setx(x)
    instance.sety(y)
    
    instance.shape(shape)
    instance.color(color)
    instance.speed(speed)
    return instance

def main():
    screen = turtle.Screen()
    screen.bgcolor(bgcolor)
    turtle_triangle = create_turtle(shape="classic", color="green", speed=5, x=-2**8, y=+2**8)
    draw_triangle(turtle_triangle, length=2**9, level=3, even_color="green", odd_color="red")
    screen.exitonclick()
    
    
main()

