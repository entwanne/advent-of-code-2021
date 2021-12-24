import sys
from itertools import product


def get_narg(arg):
    i = 'wxyz'.index(arg)
    return f'ctx[{i}]'


def parse_args(args):
    for arg in args:
        try:
            yield str(int(arg))
        except:
            yield get_narg(arg)


def execute(model, stack):
    ctx = [0, 0, 0, 0]
    for cmd, args in model:
        cargs = [eval(arg, {'ctx': ctx}) for arg in parse_args(args)]
        out = 'wxyz'.index(args[0])
        match cmd:
            case 'inp':
                ctx[out] = stack.pop(0)
                print(ctx[out])
            case 'add':
                ctx[out] = cargs[0] + cargs[1]
            case 'mul':
                ctx[out] = cargs[0] * cargs[1]
            case 'div':
                ctx[out] = cargs[0] // cargs[1]
            case 'mod':
                ctx[out] = cargs[0] % cargs[1]
            case 'eql':
                ctx[out] = int(cargs[0] == cargs[1])

    print(ctx[3] == 0)


def compute(model):
    operators = {'add': '+', 'mul': '*', 'div': '//', 'mod': '%', 'eql': '=='}

    func_content = ['def compute():', '    ctx = [0, 0, 0, 0]', '    stack = [0]*14']
    indent = '    '
    s = 0

    for cmd, args in model:
        if op := operators.get(cmd):
            a, b = parse_args(args)
            func_content.append(indent + f'{a} = int({a} {op} {b})')
        elif cmd == 'inp':
            arg, = parse_args(args)
            func_content.append(indent + f'state{s} = list(ctx)')
            func_content.append(indent + f'for stack[{s}] in range(9, 0, -1):')
            #func_content.append(indent + f'for stack[{s}] in range(1, 10):')
            indent += '    '
            if s:
                func_content.append(indent + f'if stack[{s-1}] != 9 and stack[{s}] < stack[{s-1}]: continue')
            else:
                func_content.append(indent + f'if stack[{s}] != 1: continue')
            func_content.append(indent + f'ctx = list(state{s})')
            func_content.append(indent + f'{arg} = stack[{s}]')
            s += 1

    func_content.append(indent + 'print(stack)')
    func_content.append(indent + 'if ctx[3] == 0: return stack')

    ns = {}
    print('\n'.join(func_content))
    exec('\n'.join(func_content), ns)
    return ns['compute']


model = []

for line in sys.stdin:
    cmd, *args = line.split()
    model.append((cmd, args))


stack = compute(model)()
print(''.join(map(str, stack)))
#execute(model, list(map(int, '99999999669199')))
#execute(model, list(map(int, '11111111111671')))
