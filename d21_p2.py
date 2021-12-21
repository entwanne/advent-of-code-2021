import sys
from collections import Counter
from itertools import cycle, product
from functools import cache


p1, p2 = tuple(int(line.strip().split(': ')[1]) - 1 for line in sys.stdin)

rolls = Counter(sum(r) for r in product((1, 2, 3), repeat=3))


@cache
def get_winners(p1, p2, s1=0, s2=0):
    w1, w2 = 0, 0

    for r, count in rolls.items():
        pos = (p1 + r) % 10
        score = s1 + pos + 1

        if score >= 21:
            w1 += count
        else:
            w2_, w1_ = get_winners(p2, pos, s2, score)
            w1 += count * w1_
            w2 += count * w2_

    return w1, w2


print(max(get_winners(p1, p2)))
