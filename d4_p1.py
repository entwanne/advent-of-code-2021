import sys


chosen = [int(n) for n in sys.stdin.readline().split(',')]
boards = []
width = height = 5

assert sys.stdin.readline().strip() == ''

while True:
    board = {}
    rev_board = {}
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if not line:
            break
        for x, n in enumerate(line.split()):
            board[x, y] = int(n)

    rev_board = {n: k for k, n in board.items()}
    if board:
       boards.append((board, rev_board))
    else:
        break


def find_winner():
    for n in chosen:
        for board, rboard in boards:
            key = rboard.get(n)
            if not key:
                continue
            x, y = key
            board[key] = None
            if all(board[x, j] is None for j in range(height)) or all(board[i, y] is None for i in range(width)):
                return board, n

winner, n = find_winner()
print(sum(v for v in winner.values() if v is not None) * n)
