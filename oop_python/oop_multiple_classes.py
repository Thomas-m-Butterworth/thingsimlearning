# # Working With Multiple Classes OOP

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Creating a blank list to input the student objects into
    
    def add_student(self, student): # Student argument an instance of the Student object
        if len(self.students) < self.max_students:  # Checks course max is not hit
            self.students.append(student)
            return True # Add a program later that will print if the entry was input correctly
        else:
            return False  
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

# Create students
s1 = Student("Kevin", 2, 76)
s2 = Student("Jackson", 36, 52)
s3 = Student("Josie", 60, 88)

# Create Course
course = Course("Kitten Kode", 5)

# Add Students
course.add_student(s1)
course.add_student(s2)

# print(course.get_average_grade())

## Inheritence

class Pet:  # General class
    def __init__(self, name, age):  # Define the parent init function
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name}. I am {self.age} years old")
    
    def speak(self):
        print("I don't know what to say!")

class Dog(Pet): # Takes pet class as the argument, inheriting it's functionality
    def speak(self): 
        print("Woof")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # Explicitly calls the super class attributes needs
        self.color = color
    
    def show(self):
        print(f"I am {self.name}. I am {self.age} years old! I have {self.color} fur.")

    def speak(self):
        print("Meow")

class Fish(Pet):
    pass    # Not defined yet, but parent Pet class allows basic functionality

c = Cat("Jackson", 4, "Black")
d = Dog("Rocket", 8)
f = Fish("Nemo", 2)
c.show()    # Inherited show function...
c.speak()
d.speak()   # ... but keeps it's unique function
f.speak()   # uses parent function when none is defined in the child




