class customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno
    def get_name(self):
        return self.name
    def get_phoneno(self):
        return self.phoneno
    def set_phoneno(self, ph):
        self.phoneno = ph
c1 = customer('John', 12345678)
print("Name: ", c1.get_name())
print("Phone: ", c1.get_phoneno())
c1.set_phoneno(456789123)
print("")
print("Name: ", c1.get_name())
print("Phone: ", c1.get_phoneno())
