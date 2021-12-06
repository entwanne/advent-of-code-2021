import sys

fish = [int(n) for n in sys.stdin.read().split(',')]

for _ in range(80):
    new_fish = []
    for f in fish:
        if f > 0:
            new_fish.append(f-1)
        else:
            new_fish.append(6)
            new_fish.append(8)
    fish = new_fish

print(len(fish))
