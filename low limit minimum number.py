def minimum(*values, low_limit=None):
    if low_limit is None:
        return min(values)
    else:
        L = [x for x in values if x >= low_limit]
        return min(L)
print(minimum(1, 2, 3, 4, -4, -5))