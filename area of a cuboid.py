class cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h
        
    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return 2 * (length * breadth + breadth * height + length * height)
    
    def volume(self):
        return self.length * self.breadth * self.height
    
length = int(input('Enter length: '))
breadth = int(input('Enter breadth: '))
height = int(input('Enter height: '))

c1 = cuboid(length, breadth, height)
print("The Volume is: ", c1.volume(), "\nThe Total Area is: ", c1.totalarea(), "\nThe Lidarea is: ", c1.lidarea()) 
