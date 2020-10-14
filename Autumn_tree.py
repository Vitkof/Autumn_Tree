import time
import turtle
from random import randint
# Screen setting
WIDTH, HEIGHT = 1366, 768
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(WIDTH, HEIGHT, bg='white')
screen.delay(0)
screen.bgpic('autumn.gif')

# Turtle setting
czerep = turtle.Turtle()
czerep.speed(0)

# L-system setting
gens = 10
f_strok = 'F'
ch_1, smena_1, ch_2 = 'F', 'G[@[-F]+F]', 'G'
# символ @ - осветвление текущего цвета, утоньшение и удлинение штрихов
step = 77
ygol = lambda: randint(1, 33)
color = [0.25, 0.2, 0.0]  # RGB
thickness = 19  # толщина штриха
stack = []

def zamena_simvola(ch):
    return smena_1 if ch == ch_1 else ch
def use_rules(input):
    result = ''
    for char in input:
        result += zamena_simvola(char)
    return result
def modificate_str(str, gens):
    for gen in range(gens):
        str = use_rules(str)
        print(str)
    return str
def read_char(ch, turtle):
    global step, thickness, color
    if ch == ch_1 or ch == ch_2:
        turtle.forward(step)
    elif ch == '@':  # наш гл.рандомайзер
        step -= randint(5, 7)
        color[1] += 0.05  # Green
        thickness -= randint(2, 3)
        thickness = max(1, thickness)  # дабы толщина не стала отрицательной
        turtle.pensize(thickness)
        if color[1] > 0.4:
            color[0] += 0.12  # Red
    elif ch == '+':
        turtle.right(ygol())
    elif ch == '-':
        turtle.left(ygol())
    elif ch == '[':
        _ygol, _pos = turtle.heading(), turtle.pos()
        stack.append((_ygol, _pos, step, thickness, color[0], color[1]))
    elif ch == ']':
        _ygol, _pos, step, thickness, color[0], color[1] = stack.pop()
        turtle.setheading(_ygol)
        turtle.pensize(thickness)
        turtle.penup()
        turtle.goto(_pos)
        turtle.pendown()


def main():
    turtle.pencolor('white')
    turtle.goto(-WIDTH//2 + 20, -HEIGHT//2 + 30)
    turtle.clear()
    turtle.write(f"Generation: {gens}", font=("Impact", 40, "normal"))
    turtle.up()

    czerep.up()
    czerep.goto(0, -HEIGHT//2 + 30)
    czerep.down()
    czerep.left(90)
    czerep.pensize(thickness)

    stroka = modificate_str(f_strok, gens)
    for ch in stroka:
        czerep.color(color)
        read_char(ch, czerep)
    screen.exitonclick()


if __name__ == "__main__":
    main()
