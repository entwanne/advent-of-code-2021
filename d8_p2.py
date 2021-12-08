import sys

all_segments = frozenset('abcdefg')
base_segments = {
    frozenset('abcefg'): '0',
    frozenset('cf'): '1',
    frozenset('acdeg'): '2',
    frozenset('acdfg'): '3',
    frozenset('bcdf'): '4',
    frozenset('abdfg'): '5',
    frozenset('abdefg'): '6',
    frozenset('acf'): '7',
    frozenset('abcdefg'): '8',
    frozenset('abcdfg'): '9',
}


def drop(segments, cond):
    found, = (n for n in segments if cond(n))
    segments.discard(found)
    return found


total = 0

for line in sys.stdin:
    left, right = ([frozenset(x) for x in part.split()] for part in line.split(' | '))
    mapping = {}
    left = set(left)

    one = drop(left, lambda n: len(n) == 2)
    four = drop(left, lambda n: len(n) == 4)
    seven = drop(left, lambda n: len(n) == 3)
    eight = drop(left, lambda n: len(n) == 7)

    a_seg, = seven - one
    mapping[a_seg] = 'a'

    three = drop(left, lambda n: len(n) == 5 and len(n & four) == 3 and len(n & one) == 2)
    b_seg, = four - three
    d_seg, = (three & four) - one
    mapping[b_seg] = 'b'
    mapping[d_seg] = 'd'

    nine = drop(left, lambda n: n > three)
    zero = drop(left, lambda n: n == eight - {d_seg})
    six = drop(left, lambda n: len(n) == 6)

    five = drop(left, lambda n: len(six - n) == 1)
    two = drop(left, lambda n: True)

    e_seg, = six - five
    mapping[e_seg] = 'e'
    c_seg, = eight - six
    mapping[c_seg] = 'c'
    f_seg, = six & one
    mapping[f_seg] = 'f'

    g_seg, = all_segments - mapping.keys()
    mapping[g_seg] = 'g'

    digits = (base_segments[frozenset(mapping[c] for c in n)] for n in right)
    total += int(''.join(digits))

print(total)
