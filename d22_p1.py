import sys
from itertools import product

grid = set()

for line in sys.stdin:
    state, coords = line.split()
    state = (state == 'on')

    coords = (c.split('=')[1].split('..') for c in coords.split(','))
    coords = [
        range(max(int(a), -50), min(int(b)+1, 51))
        for a, b in coords
    ]

    if state:
        grid.update(product(*coords))
    else:
        grid.difference_update(product(*coords))

print(len(grid))
