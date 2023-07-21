def func1(x,y):
    if abs(x-y) <= 5:
        return True
    else:
        return False
x = int(input('Enter a number: '))
y = int(input('Enter a number: '))
print(func1(x,y))