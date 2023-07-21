# Print prime number from a-b
a = int(input("Enter initial number"))
b = int(input("Enter last number"))
for n in range(a, b + 1):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, end=" ")
