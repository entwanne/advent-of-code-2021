import sys
from itertools import product


line = sys.stdin.read().strip().removeprefix('target area: ')
xdef, ydef = line.split(', ')
xmin, xmax = map(int, xdef.removeprefix('x=').split('..'))
ymin, ymax = map(int, ydef.removeprefix('y=').split('..'))


def check_velocity(vel):
    x, y = 0, 0
    vx, vy = vel

    while True:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
        if y < ymin:
            return False
        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1


ampl = max(abs(xmin), abs(xmax), abs(ymin), abs(ymax)) + 1


print(sum(1 for vel in product(range(ampl), range(-ampl, ampl)) if check_velocity(vel)))
