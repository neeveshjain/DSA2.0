# Method Overloading
"""Method Overloading refers to defining multiple methods in
a class with the same name but different parameters. Unlike languages
like Java, Python does not support method overloading by default.
Python achieves this through default parameters or by handling multiple
types of arguments within a single method.
"""


class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


# Usage
math_op = MathOperations()
print(math_op.add(1, 2))  # Output: 3
print(math_op.add(1, 2, 3))  # Output: 6

#-------------------------------------------------------------------------

# Method Overriding
"""Method Overriding allows a subclass to provide a specific
 implementation of a method that is already defined in its superclass. 
 This is done by defining a method in the child class with the same name 
 and signature as the one in the parent class. 
 The method in the child class will override the method in the parent class
 """


class Animal:
    def sound(self):
        return "Some generic sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Usage
generic_animal = Animal()
dog = Dog()
cat = Cat()

print(generic_animal.sound())  # Output: Some generic sound
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow