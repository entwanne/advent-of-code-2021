import sys
from collections import Counter

fish = Counter(int(n) for n in sys.stdin.read().split(','))

for _ in range(256):
    renew = fish.pop(0, 0)
    fish = Counter({n-1: v for n, v in fish.items()})
    fish[6] += renew
    fish[8] += renew

print(fish.total())
