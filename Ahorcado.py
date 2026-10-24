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


def palabra_usuario():
    print("=== JUEGO DEL AHORCADO ===")
    palabra = input("Escribe una palabra cualquiera: ").strip().lower()


    print("\n" * 30)
    return palabra


def mostrar_progreso(palabra, adivinadas):
    resultado = []

    for letra in palabra:
        if letra in adivinadas:
            resultado.append(letra)
        else:
            resultado.append("_")

    return " ".join(resultado)


def jugar():
    palabra = palabra_usuario()
    horca()

    adivinadas = set()
    falladas = set()
    fallos = 0
    max_fallos = len(partes_cuerpo)

    while fallos < max_fallos:
        print("\nPalabra:", mostrar_progreso(palabra, adivinadas))
        print(f"Fallos: {fallos}/{max_fallos}", sorted(falladas))

        letra = input("Adivina una letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Escribe solo una letra.")
            continue

        if letra in adivinadas or letra in falladas:
            print("¡Ya está! Esa letra ya la habías puesto.")
            continue

        if letra in palabra:
            adivinadas.add(letra)
            print("¡Bien!")
            if all(l in adivinadas for l in palabra):
                print(f"\n¡Ganaste! La palabra era: {palabra}")
                break
        else:
            falladas.add(letra)
            partes_cuerpo[fallos]()  
            fallos += 1
            print("Fallaste.")
    else:
        print(f"\nPerdiste. La palabra era: {palabra}")


jugar()
turtle.done()
