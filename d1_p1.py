import sys

last = None
decrease = 0

for line in sys.stdin:
    n = int(line)
    if last is not None and n > last:
        decrease += 1
    last = n

print(decrease)
