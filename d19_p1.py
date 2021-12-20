import sys
from collections import Counter, defaultdict
from itertools import product, permutations
from typing import NamedTuple


class Vec(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, rhs):
        x, y, z = self
        rx, ry, rz = rhs
        return Vec(x+rx, y+ry, z+rz)

    def __neg__(self):
        x, y, z = self
        return Vec(-x, -y, -z)

    def __sub__(self, rhs):
        return self.__add__(-rhs)

    def rotate(self, mat):
        return Vec(
            sum(mat[0][i] * self[i] for i in range(3)),
            sum(mat[1][i] * self[i] for i in range(3)),
            sum(mat[2][i] * self[i] for i in range(3)),
        )


def compute_relations(beacons):
    rel_count = Counter()
    relations = {}
    for b1, b2 in product(beacons, beacons):
        if b1 != b2:
            rel_count[b1 - b2] += 1
            relations[b1 - b2] = b1
    return rel_count, relations


def matmul(m1, m2):
    N = 3
    return tuple(
        tuple(
            sum(m1[y][i] * m2[i][x] for i in range(N))
            for x in range(N)
        )
        for y in range(N)
    )


matrixes = {
    # No rotation
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    # X-rotations
    ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
    # Y-rotations
    ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
    ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
    # Z-rotations
    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
}
perms = {matmul(m1, m2) for m1, m2 in product(matrixes, repeat=2)}

scanner_beacons = {}

scanner_id = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        scanner_id += 1
        continue
    if line.startswith('---'):
        continue

    x, y, z = map(int, line.split(','))
    scanner_beacons.setdefault(scanner_id, set()).add(Vec(x, y, z))

beacon_relations = {s: compute_relations(beacons) for s, beacons in scanner_beacons.items()}

dependencies = {}

for s1, s2 in permutations(scanner_beacons, 2):
    relations1, _ = beacon_relations[s1]
    relations2, _ = beacon_relations[s2]
    for mat in perms:
        rel2 = Counter({v.rotate(mat): c for v, c in relations2.items()})
        if (relations1 & rel2).total() >= 12 * 11:
            dependencies.setdefault(s1, set()).add((s2, mat))


scanners = {0: Vec(0, 0, 0)}
beacons = scanner_beacons[0]
nexts = [(0, s, mat) for s, mat in dependencies[0]]

while nexts:
    s1, s2, mat = nexts.pop(0)
    if s2 in scanners:
        continue
    _, rel1 = beacon_relations[s1]
    _, rel2 = beacon_relations[s2]
    new = {k.rotate(mat): v.rotate(mat) for k, v in rel2.items()}
    rel2.clear()
    rel2.update(new)

    (tvec, _), = Counter(rel1[k] - rel2[k] for k in rel2 if k in rel1).most_common(1)
    scanners[s2] = origin = scanners[s1] + tvec

    beacons.update(v.rotate(mat) + origin for v in scanner_beacons[s2])

    s1 = s2
    for s2, mat2 in dependencies.get(s1, ()):
        if s2 not in scanners:
            nexts.append((s1, s2, matmul(mat, mat2)))

print(len(beacons))
