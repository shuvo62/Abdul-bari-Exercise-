# Check if it is a leap year
year = int(input('Enter a year:'))
if year % 100 == 0 and year % 400 == 0:
    print('Leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('Leap year')
else:
    print('Not leap year')