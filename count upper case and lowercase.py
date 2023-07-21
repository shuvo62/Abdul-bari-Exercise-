def count(phrase):
    lower = 0
    upper = 0
    for l in phrase:
        if l.islower():
            lower += 1
        elif l.isupper():
            upper += 1
    return lower, upper
x = input('Enter a sentence: ')
print(count(x))

        
                        