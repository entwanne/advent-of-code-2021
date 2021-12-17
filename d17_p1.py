import sys
from itertools import product


line = sys.stdin.read().strip().removeprefix('target area: ')
xdef, ydef = line.split(', ')
xmin, xmax = map(int, xdef.removeprefix('x=').split('..'))
ymin, ymax = map(int, ydef.removeprefix('y=').split('..'))


def check_velocity(vel):
    x, y = 0, 0
    vx, vy = vel

    topy = y

    while True:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True, topy
        if y < ymin:
            return False, topy
        x += vx
        y += vy
        topy = max(topy, y)

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1


ampl = max(abs(xmin), abs(xmax), abs(ymin), abs(ymax)) + 1

checks = (check_velocity(vel) for vel in product(range(ampl), range(ampl)))
topy = max(y for check, y in checks if check)

print(topy)
