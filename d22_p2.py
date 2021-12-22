import sys
from itertools import product

ranges = []


def count(r):
    x1, x2, y1, y2, z1, z2 = r
    assert x2 >= x1
    assert y2 >= y1
    assert z2 >= z1
    return (x2 - x1) * (y2 - y1) * (z2 - z1)


def overlap(r1, r2):
    r1x1, r1x2, r1y1, r1y2, r1z1, r1z2 = r1
    r2x1, r2x2, r2y1, r2y2, r2z1, r2z2 = r2

    if max(r1x1, r2x1) > min(r1x2, r2x2):
        return
    if max(r1y1, r2y1) > min(r1y2, r2y2):
        return
    if max(r1z1, r2z1) > min(r1z2, r2z2):
        return

    return (
        max(r1x1, r2x1),
        min(r1x2, r2x2),
        max(r1y1, r2y1),
        min(r1y2, r2y2),
        max(r1z1, r2z1),
        min(r1z2, r2z2),
    )


def cut(r1, r2):
    o = overlap(r1, r2)
    if o is None:
        return [r1]

    x1, x2, y1, y2, z1, z2 = r1
    ox1, ox2, oy1, oy2, oz1, oz2 = o

    subranges = [
        r
        for (x1, x2), (y1, y2), (z1, z2) in product(
                ((x1, ox1), (ox1, ox2), (ox2, x2)),
                ((y1, oy1), (oy1, oy2), (oy2, y2)),
                ((z1, oz1), (oz1, oz2), (oz2, z2)),
        )
        if (r := (x1, x2, y1, y2, z1, z2)) != o  # overlap
    ]
    return [r for r in subranges if count(r) > 0]


def add(r):
    new = []
    for r1 in ranges:
        new.extend(cut(r1, r))
    new.append(r)
    ranges.clear()
    ranges.extend(new)


def discard(r):
    new = []
    for r1 in ranges:
        new.extend(cut(r1, r))
    ranges.clear()
    ranges.extend(new)


for N, line in enumerate(sys.stdin):
    state, coords = line.split()
    state = (state == 'on')

    coords = (c.split('=')[1].split('..') for c in coords.split(','))
    coords = [
        x
        for a, b in coords
        for x in (int(a), int(b)+1)
    ]

    if state:
        add(coords)
    else:
        discard(coords)

print(sum(count(r) for r in ranges))
