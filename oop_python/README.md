# Object Orientated Programming
My attempts to get my head around Object Orientated Programming (OOP) in Python. I am using a variety of online resources including FreeCodeCamp and Real Python.

## Objects
There are inbuilt classes in python that are used before even realising they're objects. These are functions, integers, strings, and booleans. It is possible to create our own classes, which is the nature of OOP.

## Methods
A method is performed upon an object, and rely on the type of class. (e.g. x.**strip()**, anything following the . is the method, arguments go into parenthesis)

## Creating our own classes
Define the class (in my example this is the Dog class). Define the operations that this kind of object can perform. Multiple methods can be defined within one class. By default they take the *self* argument, but others can be added (**see *add_one* in Dog.**)

## Multiple Classes
We can create multiple classes that are able to interact with eachother and complete various methods to work with themselves. *e.g* A class of students could be created, which is then input to another class representing the course the students are on. One way of acheiving this is to create blank lists for your objects to go in to.

## Inheritance
When we have two classes that are similar, it isn't clean to always repeat that functionality. Inheritance allows a function to inherit functionality from an upper-level class, and all that is define is what's different. (e.g. Removing init - See code in **oop_multiple_classes.py**)

When an inherited class needs additional attributes (e.g. We want to know the colour), write the init as you would if there were no parent class.

    ```python
    class ParentClass:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    class ChildClass(ParentClass):
        def __init__(self, name, age, color):
            super().__init__(name, age)
            self.color = color
     ```

Notice that even though the ChildClass takes multiple arguments, we only define the one that varies from ParentClass. This is because re-defining these is pointless, and can undo previous functions if not careful.

**Always try to create a general class that is the supre class to the children. Don't forget *super()*!**

## Class Attributes
Class attributes are atributed to the class itself, and not objects within them. Class atributes allow constant attributes that do not need to be added outside of the class. This effectively creates exportable classes and functions.

## Class Methods
A method is designed to be called on the class itself, not the instance. This is why it acts on (cls), not (self), as there is no object for it to refer to. 

### Static Methods
Static methods allow us to organise a large amount of functions into an organised, importable module. Similar to defining methods globally, but with the ability to standalone. It's also a life saver for organisation purposes.


