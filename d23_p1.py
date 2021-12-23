import heapq
import re
import sys

grid = {}
final_grid = {(3, 2): 'A', (3, 3): 'A', (5, 2): 'B', (5, 3): 'B', (7, 2): 'C', (7, 3): 'C', (9, 2): 'D', (9, 3): 'D'}
base_points = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

for y, line in enumerate(sys.stdin):
    for x, c in enumerate(line.rstrip()):
        if c == '#' or c == ' ':
            continue
        if c == '.':
            c = ''
        grid[x, y] = c


def can_move(grid, c, oldkey, key):
    t = grid.get(key, 'X')
    if t:
        return False
    if key in final_grid:
        if final_grid[key] == c:
            return key[1] > oldkey[1]
        else:
            return oldkey in final_grid and key[1] < oldkey[1]
    return True


def serialize(grid):
    return frozenset((x, y, c) for (x, y), c in grid.items())


def unserialize(sgrid):
    return {(x, y): c for x, y, c in sgrid}


def print_grid(grid):
    width = max(x for x, _ in grid) + 2
    height = max(y for _, y in grid) + 1
    for y in range(height):
        print(''.join(grid.get((x, y), '#') or ' ' for x in range(width)))


def solve(grid, final_grid):
    sgrid = serialize(grid)
    win_sgrid = serialize({k: '' for k in grid} | final_grid)
    dist = {sgrid: 0}
    paths = [(0, sgrid)]

    while paths:
        current, sgrid = heapq.heappop(paths)
        if sgrid in dist and dist[sgrid] < current:
            continue
        if sgrid == win_sgrid:
            break
        points = dist[sgrid]
        grid = unserialize(sgrid)

        for (x, y), c in grid.items():
            if not c:
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x+dx, y+dy
                if can_move(grid, c, (x, y), (nx, ny)):
                    p = points + base_points[c]
                    sgrid2 = sgrid - {(x, y, c), (nx, ny, '')} | {(x, y, ''), (nx, ny, c)}
                    if sgrid2 not in dist or p < dist[sgrid2]:
                        dist[sgrid2] = p
                        heapq.heappush(paths, (p, sgrid2))

    return dist[win_sgrid]


print(solve(grid, final_grid))
