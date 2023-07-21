from collections import Counter
prices = {'soap': 50, 'toothpaste': 25, 'shampo':45.50, 'toothbrush':15.99}

def generate_bill(cart):
    total = 0
    for item, qty in cart.items():
        print(f'{item:10} {prices[item]:10} x {qty:1} = {prices[item]*qty}')
        total += prices[item]*qty
        
    print(f'Total ={total:27}')
cart = Counter(soap=5, toothpaste=1, shampo=2, toothbrush=3)
generate_bill(cart)