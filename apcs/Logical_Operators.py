a, b, c, = [bool(int(x)) for x in input().split()]
is_print = True
if (a and b) == c:
    print('AND')
    is_print = False

if (a or b) == c:
    print('OR')
    is_print = False

if (a != b) == c:
    print('XOR')
    is_print = False
if is_print:
    print('IMPOSSIBLE')