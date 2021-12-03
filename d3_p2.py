import sys
from collections import Counter, defaultdict

numbers = [[int(i) for i in line.strip()] for line in sys.stdin]
o2_numbers = co2_numbers = numbers

i = 0
while len(o2_numbers) > 1:
    count = Counter(n[i] for n in o2_numbers)
    keep, _ = max(count.items(), key=lambda x: (x[1], x[0]))
    o2_numbers = [n for n in o2_numbers if n[i] == keep]
    i += 1

i = 0
while len(co2_numbers) > 1:
    count = Counter(n[i] for n in co2_numbers)
    keep, _ = min(count.items(), key=lambda x: (x[1], x[0]))
    co2_numbers = [n for n in co2_numbers if n[i] == keep]
    i += 1

o2, = o2_numbers
co2, = co2_numbers
o2 = int(''.join(map(str, o2)), 2)
co2 = int(''.join(map(str, co2)), 2)
print(o2 * co2)
