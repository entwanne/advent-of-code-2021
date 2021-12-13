import sys
from collections import Counter


graph = {}

for line in sys.stdin:
    left, right = line.strip().split('-')
    graph.setdefault(left, set()).add(right)
    graph.setdefault(right, set()).add(left)


def find_paths():
    paths = [('start',)]
    while paths:
        path = paths.pop(0)
        if path[-1] == 'end':
            yield path
            continue
        for child in graph.get(path[-1], ()):
            p = path + (child,)
            if child not in path:
                paths.append(p)
            elif not child.islower():
                paths.append(p)
            elif child not in {'start', 'end'} and not any(c > 1 for k, c in Counter(path).items() if k.islower()):
                paths.append(p)


print(sum(1 for _ in find_paths()))
