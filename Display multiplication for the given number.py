# Display multiplication for a given number
n = int(input('Enter a number: '))
counter = 1
while counter <= 10:
    print(n, 'x', counter, '=', n * counter)
    counter += 1