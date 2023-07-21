# Fibonacci series (0,1,1,2,3,5,8....)
n = int(input('Enter terms'))
a = 0
b = 1
for i in range (n):
  print(a)
  c  = a+b
  a = b
  b = c