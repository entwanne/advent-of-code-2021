import sys
import statistics

crabs = [int(c) for c in sys.stdin.read().split(',')]
m = int(statistics.median(crabs))
print(sum(abs(c - m) for c in crabs))
