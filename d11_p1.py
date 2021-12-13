import sys
from itertools import product


grid = {
    (x, y): int(n)
    for y, line in enumerate(sys.stdin)
    for x, n in enumerate(line.strip())
}

nb_flashed = 0
steps = 100


for _ in range(steps):
    grid = {k: o+1 for k, o in grid.items()}
    all_flashed = set()
    while flashed := {k for k, o in grid.items() if o > 9}:
        all_flashed.update(flashed)
        for k in flashed:
            x, y = k
            grid[k] = 0
            for dx, dy in product((-1, 0, 1), repeat=2):
                nk = x+dx, y+dy
                if nk in grid and nk not in all_flashed:
                    grid[nk] += 1

    nb_flashed += len(all_flashed)


print(nb_flashed)
