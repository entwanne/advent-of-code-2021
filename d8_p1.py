import sys
from collections import Counter


count = Counter()


for line in sys.stdin:
    _, right = line.split(' | ')
    count.update(len(x) for x in right.split())

print(count[2] + count[4] + count[3] + count[7]) # 1 + 4 + 7 + 8
