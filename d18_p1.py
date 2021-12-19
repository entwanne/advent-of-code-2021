import sys
from math import ceil


class Number:
    def __init__(self, n, level):
        self.n = n
        self.level = level


def flatten(pair, ret=None, level=0):
    if ret is None:
        ret = []
    if isinstance(pair, int):
        ret.append(Number(pair, level))
        return ret
    left, right = pair
    flatten(left, ret, level+1)
    flatten(right, ret, level+1)
    return ret


def unflatten(numbers):
    result = []
    queue = [result]
    for num in numbers:
        while len(queue) < num.level:
            new = []
            queue[-1].append(new)
            queue.append(new)
        queue[-1].append(num.n)
        while queue and len(queue[-1]) == 2:
            del queue[-1]
    return result


def explode(numbers):
    i, left = next(
        ((i, n) for i, n in enumerate(numbers) if n.level == 5 and numbers[i+1].level == 5),
        (None, None),
    )
    if left is None:
        return
    right = numbers.pop(i+1)
    if i > 0:
        numbers[i-1].n += left.n
    if i < len(numbers) - 1:
        numbers[i+1].n += right.n
    numbers[i].n = 0
    numbers[i].level -= 1
    return True


def split(numbers):
    i, num = next(
        ((i, n) for i, n in enumerate(numbers) if n.n >= 10),
        (None, None),
    )
    if num is None:
        return
    num.level += 1
    right = Number(ceil(num.n / 2), num.level)
    num.n //= 2
    numbers.insert(i+1, right)
    return True


def reduce(numbers):
    while explode(numbers) or split(numbers):
        pass
    return numbers


def addition(n1, n2):
    return reduce([
        Number(num.n, num.level+1)
        for num in n1 + n2
    ])


def magnitude(pair):
    if isinstance(pair, int):
        return pair
    left, right = pair
    return 3 * magnitude(left) + 2 * magnitude(right)


current = None
for line in sys.stdin:
    numbers = reduce(flatten(eval(line)))
    if current is None:
        current = numbers
    else:
        current = addition(current, numbers)

pair = unflatten(current)
print(magnitude(pair))
