# class Person:
#     number_of_people = 0    # This is the class attribute, does not use self

#     def __init__(self, name):
#         self.name = name
#         Person.add_person() # Tracks how many instances we've created of this class

#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1


# p1 = Person("Thom")
# p2 = Person("Kat")


# print(Person.number_of_people_())

### Static Methods

class Math:
    
    @staticmethod
    def add42(x):
        return x + 42

print(Math.add42(9))
