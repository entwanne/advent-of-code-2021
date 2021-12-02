import sys

pos = depth = aim = 0

for line in sys.stdin:
    cmd, arg = line.split()
    arg = int(arg)
    if cmd == 'forward':
        pos += arg
        depth += aim * arg
    elif cmd == 'down':
        aim += arg
    elif cmd == 'up':
        aim -= arg

print(pos * depth)
