import time
import turtle
# Screen setting
WIDTH, HEIGHT = 1366, 768
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(WIDTH, HEIGHT, bg='white')
screen.delay(0)

# Turtle setting
czerep = turtle.Turtle()
czerep.pensize(2)
czerep.speed(0)
czerep.color('blue')
#czerep.setpos(-WIDTH//3, -HEIGHT//2)
# L-system setting
gens = 7
f_strok = 'F'
ch_1, smena_1 = 'F', 'F-G+F+G-F'
ch_2, smena_2 = 'G', 'GG'
step = 6
ygol = 120

def apply_rule(input):
    lst = [smena_1 if ch == ch_1 else smena_2 for ch in input]
    return ''.join(lst)
def zamena_simvola(ch):
    if ch == ch_1:
        return smena_1
    elif ch == ch_2:
        return smena_2
    else:
        return ch
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
    if ch == ch_1:
        turtle.forward(step)
    elif ch == ch_2:
        turtle.forward(step)
    elif ch == '+':
        turtle.right(ygol)
    elif ch == '-':
        turtle.left(ygol)


def main():
    turtle.pencolor('black')
    turtle.goto(-WIDTH//2 + 320, -HEIGHT//2 + 20)
    turtle.clear()
    turtle.write(f"Generation: {gens}", font=("Impact", 40, "normal"))
    #czerep.setheading(0)
    czerep.up()
    czerep.goto(-WIDTH//2 + 350, -HEIGHT//2 + 83)
    czerep.down()

    stroka = modificate_str(f_strok, gens)
    for ch in stroka:
        read_char(ch, czerep)
    screen.exitonclick()

if __name__ == "__main__":
    main()