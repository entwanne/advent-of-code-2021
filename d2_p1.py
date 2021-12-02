import sys

pos = depth = 0

for line in sys.stdin:
    cmd, arg = line.split()
    arg = int(arg)
    if cmd == 'forward':
        pos += arg
    elif cmd == 'down':
        depth += arg
    elif cmd == 'up':
        depth -= arg

print(pos * depth)
