# Finding roots of quadratic equation:
# Have to give proper imports. if math root becomes negative then it will show an error.

import math
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
r1 = (- b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
r2 = (- b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print('Your roots are', r1, r2)
