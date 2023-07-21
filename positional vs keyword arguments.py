def net_sal(basic, allowences, deduction):
    net = basic + allowences - deduction
    return net

n = net_sal(8000,6000,2000)
print('Net salary is', n)