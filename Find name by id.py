def name(id):
    names = {1: 'shuvo', 2: 'sharna', 3: 'abbu', 4: 'ammu', 5: 'mijan', 6: 'rasel', 7: 'rayhan'};
    if id in names:
        return names[id]
    else:
        return 'not in the list'

id = int(input('Enter an ID: '));
print('The name is', name(id))