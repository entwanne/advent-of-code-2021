import sys
import statistics
from collections import Counter


def additional(n):
    return sum(range(0, n))

crabs = [int(c) for c in sys.stdin.read().split(',')]
M = round(statistics.mean(crabs))
mr = range(M-20, M+21)

print(min(sum(additional(abs(c - m) + 1) for c in crabs) for m in mr))
