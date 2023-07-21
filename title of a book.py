class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def show_details(self):
        print ("Title: ", self.title)
        print ("Author: ", self.author)
        print ("Price: ", self.price)

c1 = book("Python Book", "The Great Shuvoda", "160 TK")
print (c1.show_details())

c2 = book("Matlab book", "The Great Shuvoda", "170 TK")
print (c2.show_details())