import sys


mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
rev_mapping = {v: k for k, v in mapping.items()}

char_points = dict(zip(mapping, range(1, len(mapping)+1)))

opening_chars = set(mapping)
closing_chars = set(rev_mapping)

all_points = []


for line in sys.stdin:
    opening = []
    for c in line.strip():
        if c in opening_chars:
            opening.append(c)
        elif c in closing_chars:
            oc = opening.pop() if opening else None
            if oc != rev_mapping[c]:
                break
    else:
        points = 0
        while opening:
            oc = opening.pop()
            points = points * 5 + char_points[oc]
        all_points.append(points)

all_points.sort()
print(all_points[len(all_points) // 2])
