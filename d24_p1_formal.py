import operator
import sys
from itertools import count


def parse_args(ctx, args):
    for arg in args:
        if arg in ctx:
            yield ctx[arg]
        else:
            yield int(arg)


def check(expr, n):
    return isinstance(expr, int) and expr == n


def nminmax(n):
    if isinstance(n, int):
        return n, n
    return n.min, n.max


def nmin(n):
    min_, _ = nminmax(n)
    return min_


def nmax(n):
    _, max_ = nminmax(n)
    return max_


class _Expr:
    min = max = None

    def __add__(self, rhs):
        return add(self, rhs)

    def __radd__(self, lhs):
        return add(lhs, self)

    def __mul__(self, rhs):
        return mul(self, rhs)

    def __rmul__(self, lhs):
        return mul(lhs, self)

    def __floordiv__(self, rhs):
        return div(self, rhs)

    def __rfloordiv__(self, lhs):
        return div(lhs, self)

    def __mod__(self, rhs):
        return mod(self, rhs)

    def __rmod__(self, lhs):
        return mod(lhs, self)

    def __eq__(self, rhs):
        return eq(self, rhs)


class _BinOp(_Expr):
    def __init__(self, char, op, lhs, rhs, min, max):
        self.char = char
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        self.min = min
        self.max = max

    def __repr__(self):
        return f'({self.lhs} {self.char} {self.rhs})'


def add(lhs, rhs):
    if check(lhs, 0):
        return rhs
    if check(rhs, 0):
        return lhs
    return _BinOp(
        '+', operator.add, lhs, rhs,
        min=nmin(lhs)+nmin(rhs),
        max=nmax(lhs)+nmax(rhs),
    )


def mul(lhs, rhs):
    if check(lhs, 0) or check(rhs, 0):
        return 0
    if check(lhs, 1):
        return rhs
    if check(rhs, 1):
        return lhs
    if isinstance(lhs, int):
        if isinstance(rhs, _BinOp) and rhs.char == '+':
            return add(mul(lhs, rhs.lhs), mul(lhs, rhs.rhs))
        if isinstance(rhs, _BinOp) and rhs.char == '*':
            if isinstance(rhs.lhs, int):
                return mul(lhs * rhs.lhs, rhs.rhs)
            elif isinstance(rhs.rhs, int):
                return mul(rhs.lhs, lhs * rhs.rhs)
    elif isinstance(rhs, int):
        if isinstance(lhs, _BinOp) and lhs.char == '+':
            return add(mul(lhs.lhs, rhs), mul(lhs.rhs, rhs))
        if isinstance(lhs, _BinOp) and lhs.char == '*':
            if isinstance(lhs.lhs, int):
                return mul(lhs.lhs * rhs, lhs.rhs)
            elif isinstance(lhs.rhs, int):
                return mul(lhs.lhs, lhs.rhs * rhs)

    min1, max1 = nminmax(lhs)
    min2, max2 = nminmax(rhs)
    vals = [min1*min2, min1*max2, max1*min2, max1*max2]
    if min1 <= 0 <= max1 or min2 <= 0 <= max2:
        vals.append(0)
    return _BinOp(
        '*', operator.mul, lhs, rhs,
        min=min(vals),
        max=max(vals),
    )


def div(lhs, rhs):
    if check(lhs, 0):
        return 0
    if check(rhs, 0):
        raise ZeroDivisionError
    if check(rhs, 1):
        return lhs

    min1, max1 = nminmax(lhs)
    min2, max2 = nminmax(rhs)
    if min1 >= 0 and min2 > 0:
        min3 = min1 // max2
        max3 = max1 // min2
    elif max1 <= 0 and max2 < 0:
        min3 = min1 // max2
        max3 = max1 // min2
    elif min1 >= 0:
        min3 = max1 // min2
        max3 = max1 if max2 > 0 else 0
    else:
        min3 = min(-1, nmin(lhs)),
        max3 = max(0, nmax(lhs)),
    return _BinOp(
        '//', operator.floordiv, lhs, rhs,
        min=min3,
        max=max3,
    )


def mod(lhs, rhs):
    if check(lhs, 0):
        return 0
    if check(rhs, 0):
        raise ZeroDivisionError
    if check(rhs, 1):
        return 0
    min1 = max(nmin(lhs), 0)
    min2 = max(nmin(rhs), 1)
    return _BinOp(
        '%', operator.mod, lhs, rhs,
        min=min1 if min1 < min2 else 0,
        max=nmax(rhs)-1,
    )


def eq(lhs, rhs):
    if nmax(lhs) < nmin(rhs) or nmin(lhs) > nmax(rhs):
        return False
    if nmin(lhs) == nmax(lhs) == nmin(rhs) == nmax(rhs):
        return True
    return _BinOp(
        '==', operator.eq, lhs, rhs,
        min=0, max=1,
    )


class Sym(_Expr):
    def __init__(self, name):
        self.name = name
        self.min = 1
        self.max = 9

    def __repr__(self):
        return f's_{self.name}'


def gen_symbols():
    for i in count():
        yield Sym(i)


def execute(model):
    ctx = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    symbols = gen_symbols()
    for cmd, args in model:
        cargs = tuple(parse_args(ctx, args))
        out = args[0]
        match cmd:
            case 'inp':
                ctx[out] = next(symbols)
            case 'add':
                ctx[out] = cargs[0] + cargs[1]
            case 'mul':
                ctx[out] = cargs[0] * cargs[1]
            case 'div':
                ctx[out] = cargs[0] // cargs[1]
            case 'mod':
                ctx[out] = cargs[0] % cargs[1]
            case 'eql':
                ctx[out] = (cargs[0] == cargs[1])

        #print(cmd, args, cargs)
        #print(ctx['z'])

    return ctx['z']
    #return ctx


model = []

for line in sys.stdin:
    cmd, *args = line.split()
    model.append((cmd, args))


#print(execute(model))
res = execute(model)
print(res)
print(res.min, res.max)
#print(type(res))
#print(type(res.lhs))
#print(type(res.rhs))
