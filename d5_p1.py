import sys
from collections import Counter

grid = Counter()

for line in sys.stdin:
    x1, y1, x2, y2 = map(int, line.replace('->', '').replace(',', ' ').split())
    if x1 == x2:
        y1, y2 = sorted((y1, y2))
    elif y1 == y2:
        x1, x2 = sorted((x1, x2))
    else:
        continue

    xr = range(x1, x2+1)
    yr = range(y1, y2+1)
    for y in yr:
        for x in xr:
            grid[x, y] += 1

print(sum(1 for v in grid.values() if v > 1))
