# Check if a student is pass of fail in 3 subject:
math = int(input('Enter Math Marks: '))
Physics = int(input('Enter Physics Marks: '))
Chemistry = int(input('Enter Chemistry Marks: '))
if math >= 45 and Physics >= 45 and Chemistry >= 45:
    print('Pass')
else:
    print('fail')


