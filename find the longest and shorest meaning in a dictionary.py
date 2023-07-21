dict1 = {'piece': 'lkasjdin iahsdfkj uioashvkj zvoiafjnkasdc king',
         'puzzle': 'kjasdf iei asdkhfjs',
         'picture':'fuckoins de'}
keys = list(dict1.keys())
values = list(dict1.values())
lens = [len(x) for x in values]

max_len = max(lens)
min_len = min(lens)

max_index = lens.index(max_len)
min_index = lens.index(min_len)

print('Max lens', keys[max_index], values[max_index])
print('Min lens', keys[min_index], values[min_index])
