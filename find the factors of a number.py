# Factors (gunoniyok).
n = int(input('Enter a number: '))
# nothing can divided by zero
for i in range(1,n+1):
  if n % i == 0:
    print(i)