import random
n = random.randint(1,10)
guess = 0
while guess != n:
  guess = int(input('Enter a number: '))
  if guess > n:
    print('The number is bigger')
  elif guess < n:
    print('The number is lesser')
  else:
    print('Hurrah!, you got the correct number')
