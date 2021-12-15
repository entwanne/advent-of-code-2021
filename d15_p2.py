import sys
from itertools import product


basegrid = {
    (x, y): int(n)
    for y, line in enumerate(sys.stdin)
    for x, n in enumerate(line.strip())
}
width = max(x for x, _ in basegrid) + 1
height = max(y for _, y in basegrid) + 1
grid = {}

for (x, y), n in basegrid.items():
    for bx, by in product(range(5), repeat=2):
        bn = ((n-1) + bx + by) % 9 + 1
        grid[bx * width + x, by * height + y] = bn

start = (0, 0)
target = max(grid)

dist = {start: 0}
paths = [start]
while paths:
    node = paths.pop(0)
    risk = dist[node]
    x, y = node
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        key = x+dx, y+dy
        if key in grid:
            r = risk + grid[key]
            if key not in dist or r < dist[key]:
                dist[key] = r
                paths.append(key)

print(dist[target])
