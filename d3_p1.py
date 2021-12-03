import sys
from collections import Counter, defaultdict

bits = defaultdict(Counter)
bitlength = 0

for line in sys.stdin:
    line = line.strip()[::-1]
    bitlength = len(line)
    for i, bit in enumerate(line):
        bits[i][int(bit)] += 1


gamma = sum(b.most_common()[0][0] * 2**i for i, b in bits.items())
mask = int('1'*bitlength, 2)
epsilon = ~gamma & mask
print(gamma * epsilon)
