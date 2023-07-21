# Sum of the given number in inputs:
# num_of_numbers = int(input('Enter number of numbers: '))
# sum = 0
# count = 0
# while count < num_of_numbers:
#   n = int(input('Enter a number'))
#   sum = sum + n
#   count += 1
# print('Your sum is', sum)

# Sum of the positive and negative numbers in input:
num_of_numbers = int(input('Enter number of numbers'))
psum = 0
nsum = 0
count = 0
while count < num_of_numbers:
  n = int(input('Enter a number'))
  if n > 0:
    psum = psum + n
  else:
    nsum = nsum + n
  count = count + 1
print('The positive number is:', psum)
print('The negative number is:', nsum)
  
  

