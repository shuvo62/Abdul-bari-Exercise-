from collections import Counter

inventory =  Counter(apple=100, banana=100, pineapple=100, orange=100)

def update_inventory(order):
    
    inventory.subtract(order)

order = Counter(apple=10, banana=14, pineapple=10, orange=10)
update_inventory(order)

print(inventory)


