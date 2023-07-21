def invert(d):
    newd = {}
    for k, v in d.items():
        newd[v] = k
    return newd
D1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
D2 = invert(D1)
print (D2)