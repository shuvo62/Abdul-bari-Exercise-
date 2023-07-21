# Check if a name can admin authorized
username = input('Enter a name: ')
if username == 'john' or username == 'smith' or username == 'John' or username == 'Smith':
    print('Access Confirmed')
else:
    print('Access Denied')
