import sys


paper = set()


for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    x, y = map(int, line.split(','))
    paper.add((x, y))


fold = sys.stdin.readline().strip().removeprefix('fold along ')
dim, k = fold.split('=')
dim = 0 if dim == 'x' else 1
k = int(k)


page1 = {p for p in paper if p[dim] < k}
page2 = {p for p in paper if p[dim] > k}
page2 = {
    (2*k - x, y) if dim == 0 else (x, 2*k - y)
    for x, y in page2
}
print(len(page1 | page2))
