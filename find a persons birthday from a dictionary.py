birthdays = {'Sachin' : '10/02/2001',
             'Shuvo': '01/01/2001',
             'Shopna': '02/03/2011',
             'Sharna': '25/03/2007'
             }
name = input('Enter name: ')
if name in birthdays:
    print('Mr/Mrs {} is on {}'.format(name, birthdays[name]))
else:
    print('Name is not found')