print("Ho Huu Manh")
print("Msv:235752021610035")
import turtle

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    pen = turtle.Turtle()
    pen.color("red")
    pen.pensize(2)

    pen.circle(50)

    window.mainloop()

draw_circle()
