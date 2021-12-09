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
print(sum(v+1 for v in low_points.values()))
