# Counting the number of digits in a number
n = int(input('Enter a number: '))
counter = 0
while n:
    n = n // 10
    counter += 1
print('Number of digits are:', counter)
