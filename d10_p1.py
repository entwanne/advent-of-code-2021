import sys


mapping = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

closing_chars = set(mapping)
opening_chars = set(mapping.values())

points = 0


for line in sys.stdin:
    opening = []
    for c in line.strip():
        if c in opening_chars:
            opening.append(c)
        elif c in closing_chars:
            oc = opening.pop() if opening else None
            if oc != mapping[c]:
                points += char_points.get(c, 0)
                break

print(points)
