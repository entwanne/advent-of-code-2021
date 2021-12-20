import sys
from collections import defaultdict
from itertools import product


algo = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    algo += [1 if c == '#' else 0 for c in line]

grid = defaultdict(int)

for y, line in enumerate(sys.stdin):
    line = line.strip()
    for x, c in enumerate(line):
        grid[x, y] = 1 if c == '#' else 0


def expand(grid):
    minx = min(x for x, _ in grid)
    maxx = max(x for x, _ in grid)
    miny = min(y for _, y in grid)
    maxy = max(y for _, y in grid)

    default = grid[None, None]
    if default:
        default = 0b111111111
    default = algo[default]
    new = defaultdict(lambda: default)

    for y, x in product(range(miny-1, maxy+2), range(minx-1, maxx+2)):
        bits = (grid[x+dx, y+dy] for dy, dx in product(range(-1, 2), repeat=2))
        bits = list(bits)
        n = int(''.join(map(str, bits)), 2)
        new[x, y] = algo[n]

    return new


grid = expand(grid)
grid = expand(grid)

print(sum(1 for v in grid.values() if v))
