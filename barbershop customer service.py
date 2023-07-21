from collections import deque
customers = deque()
def walk_in(customer):
    customers.append(customer)

def serviced():
    # cust = customers.popleft()
    print(customers.popleft(), 'Leaves the shop')

walk_in('John')
walk_in('Smith')
walk_in('Shuvo')
serviced()
serviced()
print(customers)


