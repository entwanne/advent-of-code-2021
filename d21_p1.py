import sys
from itertools import cycle


players = [int(line.strip().split(': ')[1]) - 1 for line in sys.stdin]
scores = [0 for _ in players]
dice = cycle(range(1, 101))
roll_count = 0

def roll(n=1):
    global roll_count
    roll_count += n
    return sum(next(dice) for _ in range(n))

while all(score < 1000 for score in scores):
    for p, player in enumerate(players):
        r = roll(3)
        player = (player + r) % 10
        players[p] = player
        scores[p] += player + 1
        if scores[p] >= 1000:
            break

print(min(scores) * roll_count)
