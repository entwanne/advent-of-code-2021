import sys


paper = set()


for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    x, y = map(int, line.split(','))
    paper.add((x, y))


for line in sys.stdin:
    fold = line.strip().removeprefix('fold along ')
    dim, k = fold.split('=')
    dim = 0 if dim == 'x' else 1
    k = int(k)

    page1 = {p for p in paper if p[dim] < k}
    page2 = {p for p in paper if p[dim] > k}
    page2 = {
        (2*k - x, y) if dim == 0 else (x, 2*k - y)
        for x, y in page2
    }
    paper = page1 | page2


width = max(x for x, _ in paper) + 1
height = max(y for _, y in paper) + 1

for y in range(height):
    print(' '.join('#' if (x, y) in paper else ' ' for x in range(width)))
