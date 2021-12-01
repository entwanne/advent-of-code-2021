import sys
from itertools import count

windows = {}
markers = count()
increase = 0
last = None

for line in sys.stdin:
    n = int(line)
    windows[next(markers)] = []
    for marker, depths in list(windows.items()):
        depths.append(n)
        if len(depths) >= 3:
            del windows[marker]
            s = sum(depths)
            if last is not None and s > last:
                increase += 1
            last = s

print(increase)
