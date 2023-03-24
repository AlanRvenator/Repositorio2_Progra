from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
"Variables que utilizamos"
taps2 = 0
impar = 0

def square(x, y, c):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    "Cambiar el color del tablero para que fuera inovador"
    if (c == 1):
        color('black', 'cyan')
    else:
        color('black', 'red')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global taps2 
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    "Imprimir los taps"
    taps2 = taps2 + 1
    print(taps2)


def draw():
    global taps2 
    global impar
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            impar = (count%2)
            square(x, y,impar)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        "Centrar el tecto a los cuadros"
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')
        
    "Dibujar los taps"
    up()
    goto(-230, 180)
    color('black')
    write(taps2, font=('Arial', 15, 'normal'), align='left')

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(480, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()