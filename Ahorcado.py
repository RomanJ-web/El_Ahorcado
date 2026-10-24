import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(4)
t.hideturtle()


def horca():
    t.penup()
    t.goto(-100, -150)
    t.pendown()

    t.forward(200)
    t.backward(150)

    t.left(90)
    t.forward(300)

    t.right(90)
    t.forward(100)

    t.right(90)
    t.forward(40)


def cabeza():
    t.penup()
    t.goto(50, 70)
    t.setheading(0)
    t.pendown()
    t.circle(20)


def torso():
    t.penup()
    t.goto(50, 70)
    t.setheading(270)
    t.pendown()
    t.forward(70)


def brazo_izquierdo():
    t.penup()
    t.goto(50, 50)
    t.setheading(225)
    t.pendown()
    t.forward(40)


def brazo_derecho():
    t.penup()
    t.goto(50, 50)
    t.setheading(315)
    t.pendown()
    t.forward(40)


def pierna_izquierda():
    t.penup()
    t.goto(50, 0)
    t.setheading(240)
    t.pendown()
    t.forward(50)


def pierna_derecho():
    t.penup()
    t.goto(50, 0)
    t.setheading(300)
    t.pendown()
    t.forward(50)


partes_cuerpo = [
    cabeza,
    torso,
    brazo_izquierdo,
    brazo_derecho,
    pierna_izquierda,
    pierna_derecho,
]

horca()

for parte in partes_cuerpo:
    parte()
    
turtle.done()
