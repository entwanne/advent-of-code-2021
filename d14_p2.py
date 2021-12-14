import sys
from collections import Counter

tpl = sys.stdin.readline().strip()
rules = {}

sys.stdin.readline()

for line in sys.stdin:
    (a, b), c = line.strip().split(' -> ')
    rules[a, b] = c

pairs = Counter(zip(tpl, tpl[1:]))

for _ in range(40):
    new = Counter()
    for pair, n in pairs.items():
        r = rules[pair]
        a, b = pair
        new[a, r] += n
        new[r, b] += n
    pairs = new

count = Counter()
for (_, b), n in pairs.items():
    count[b] += n

count[tpl[0]] += 1

(_, x), *_, (_, y) = count.most_common()
print(x - y)
