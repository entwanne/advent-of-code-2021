import sys

grid = {}

for y, line in enumerate(sys.stdin):
    for x, c in enumerate(line.strip()):
        if c == '>':
            grid[x, y] = 'right'
        elif c == 'v':
            grid[x, y] = 'down'

width = x+1
height = y+1

N = 0

while True:
    N += 1
    old, new = dict(grid), {}

    for (x, y), d in grid.items():
        if d == 'right':
            nx = (x + 1) % width
            if not grid.get((nx, y)):
                new[x, y] = None
                new[nx, y] = 'right'

    grid |= new
    new = {}

    for (x, y), d in grid.items():
        if d == 'down':
            ny = (y + 1) % height
            if not grid.get((x, ny)):
                new[x, y] = None
                new[x, ny] = 'down'

    grid |= new

    if grid == old:
        break

print(N)
