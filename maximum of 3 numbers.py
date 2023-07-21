def max(x,y,z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z
x  = int(input('Enter a number: '))
y =  int(input('Enter a number: '))
z = int(input('Enter a number: '))
print(max(x,y,z))