class NegativeAgeException(Exception):
    pass
def stage(age):
    if age < 0:
        raise NegativeAgeException('Age must be positive')
    elif age >= 0 and age < 13:
        print('kids')
    elif age >=13 and age < 20:
        print('Teens')
    elif age >=20 and age < 50:
        print('Young')
    else:
        print('old')
age = int(input('Enter your age: '))
try:
    stage(age)
except NegativeAgeException as e:
    print(e)
    
    