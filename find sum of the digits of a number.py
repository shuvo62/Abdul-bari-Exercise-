# Sum the digits of a number
n = int(input('Enter a number: '))
sum = 0
while n > 0:
  r = n % 10
  n = n // 10
  sum = sum + r
print(sum)