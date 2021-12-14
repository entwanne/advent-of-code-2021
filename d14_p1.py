import sys
from collections import Counter

tpl = sys.stdin.readline().strip()
rules = {}

sys.stdin.readline()

for line in sys.stdin:
    (a, b), c = line.strip().split(' -> ')
    rules[a, b] = c

poly = list(tpl)

for _ in range(10):
    new = poly[:1]
    for p in poly[1:]:
        r = rules[new[-1], p]
        new.append(r)
        new.append(p)
    poly = new

count = Counter(poly)
(_, x), *_, (_, y) = count.most_common()
print(x - y)
