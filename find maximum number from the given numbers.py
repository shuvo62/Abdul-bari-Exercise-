# Find maximum number from the given number
num_of_numbers = int(input('Enter number of numbers: '))
max = int(input('Enter a number'))
count = 0
while count < num_of_numbers - 1:
  n = int(input('Enter a number'))
  if n > max:
    max = n
  count += 1
print(max)