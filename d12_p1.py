import sys


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
            if not child.islower() or child not in path:
                p = path + (child,)
                paths.append(p)


print(sum(1 for _ in find_paths()))
