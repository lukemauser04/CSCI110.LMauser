import turtle
def draw_square(t, sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("5 Squares")
luke = turtle.Turtle()
luke.color("hotpink")
luke.pensize(3)
draw_square(luke, 20)
luke.penup()
for i in range (1):
    luke.back(10)
    luke.right(90)
    luke.forward(10)
    luke.left(90)

    
draw_square(luke, 40)
luke.pendown()
draw_square(luke, 40)
luke.penup()
for i in range (1):
    luke.back(10)
    luke.right(90)
    luke.forward(10)
    luke.left(90)

    
luke.pendown()
draw_square(luke, 60)
luke.penup()
for i in range (1):
    luke.back(10)
    luke.right(90)
    luke.forward(10)
    luke.left(90)

    
luke.pendown()
draw_square(luke, 80)
luke.penup()
for i in range (1):
    luke.back(10)
    luke.right(90)
    luke.forward(10)
    luke.left(90)

    
luke.pendown()
draw_square(luke, 100)
