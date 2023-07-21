def pangram(phrase):
    letter = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '}
    phrase = set(phrase.lower())
    if phrase >= letter:
        return 'Pangram'
    else:
        return 'Not a Pangram'
x = input('Enter a sentence: ')
print(pangram(x))
    