try:
    a = int(input('Enter a number: '))
    b = int(input('Enter second number: '))
    c = a // b
    print('Try block execute successfully')
except ZeroDivisionError as err:
    print(err)
else:
    print(c)

    