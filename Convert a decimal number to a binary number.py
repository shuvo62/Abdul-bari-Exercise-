# Convert a decimal number to a binary number
n = int(input('Enter a number: '))
bin = 0
while n > 0:
  r = n % 2
  n = n// 2
  bin = bin * 10 + r

rev = 0
while bin > 0:
  r = bin % 10
  bin = bin // 10
  rev = rev * 10 + r
print(rev)