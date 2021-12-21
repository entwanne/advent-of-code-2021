import sys
from collections import Counter
from itertools import cycle, product


players = tuple(int(line.strip().split(': ')[1]) - 1 for line in sys.stdin)
scores = tuple(0 for _ in players)

univers = Counter([(players, scores, 0)])
winners = Counter()

rolls = Counter(sum(r) for r in product((1, 2, 3), repeat=3))

while univers:
    (players, scores, p), n = univers.popitem()
    np = (p + 1) % len(players)

    for r, count in rolls.items():
        pos = (players[p] + r) % 10
        players_ = list(players)
        scores_ = list(scores)
        players_[p] = pos
        scores_[p] += pos + 1
        if scores_[p] >= 21:
            winners[p] += n * count
        else:
            univers[tuple(players_), tuple(scores_), np] += n * count

print(max(winners.values()))
