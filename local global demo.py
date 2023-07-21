g = 10
def fun1(a,b):
    c = a + b
    print('local', c)
    print('global', g)
fun1(4,8)