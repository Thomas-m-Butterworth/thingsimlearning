#Object Orientated Programming

# Define a class
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Tony", 34)
d.set_age(27)
print(d.get_name())

## Second object created using the same class
# d2 = Dog("Kevin", 8)
# print(d2.get_name())

print(f"Meet {d.name}. They are {d.age} years old!")