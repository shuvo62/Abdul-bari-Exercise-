# AP meand arithmatics progression (4, 9, 14, 19, 24, 29, 34, 39):
a = int(input('Enter initial number'))
d = int(input('Enter common difference'))
n = int(input('Enter number of terms'))
for t in range(a,a + n * d,d):
  print(t)