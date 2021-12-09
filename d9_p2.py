import sys


def is_low(grid, x, y):
    c = grid[x, y]
    nexts = {
        grid.get((x-1, y), 10),
        grid.get((x+1, y), 10),
        grid.get((x, y-1), 10),
        grid.get((x, y+1), 10),
    }
    return all(c < x for x in nexts)

def find_bassin(grid, x, y):
    keys = [(x, y)]
    seen = set()
    while keys:
        x, y = keys.pop(0)
        seen.add((x, y))
        nexts = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        nexts = (n for n in nexts if n not in seen and grid.get(n, 9) != 9)
        keys.extend(nexts)
    return len(seen)

grid = {
    (x, y): int(c)
    for y, line in enumerate(sys.stdin)
    for x, c in enumerate(line.strip())
}

low_points = {
    (x, y): height
    for (x, y), height in grid.items()
    if is_low(grid, x, y)
}
bassins = sorted(find_bassin(grid, x, y) for x, y in low_points)
print(bassins[-1] * bassins[-2] * bassins[-3])
