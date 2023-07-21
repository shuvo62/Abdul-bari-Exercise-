def sum0(L):
    s = 0
    for e in L:
        if e % 10 == 0:
            s += e
    return s
L = [int(x) for x in input('Enter numbers with space: ').split(' ')]
print(sum0(L))