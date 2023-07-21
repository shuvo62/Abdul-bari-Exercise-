# Check who is eldest.
John = float(input('Enter age of John: '))
Shuvo = float(input('Enter age of Shuvo: '))
Sharna = float(input('Enter age of Sharna: '))
if John > Shuvo and John > Sharna:
    print('John is elder')
elif Shuvo > Sharna:
    print('Shuvo is elder')
else:
    print('Sharna is elder')