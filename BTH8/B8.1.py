import turtle
print("Ho Huu Manh")
print("Msv:235752021610035")
def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.color("blue")
    pen.pensize(2)

    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    window.mainloop()

draw_square()
