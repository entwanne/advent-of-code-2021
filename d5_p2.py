import sys
from collections import Counter

grid = Counter()

for line in sys.stdin:
    x1, y1, x2, y2 = map(int, line.replace('->', '').replace(',', ' ').split())

    if x1 == x2:
        dx = 0
    elif x1 < x2:
        dx = 1
    else:
        dx = -1

    if y1 == y2:
        dy = 0
    elif y1 < y2:
        dy = 1
    else:
        dy = -1

    x, y = x1, y1
    while (x, y) != (x2, y2):
        grid[x, y] += 1
        x, y = x+dx, y+dy
    grid[x, y] += 1

print(sum(1 for v in grid.values() if v > 1))
