# Hierachical Inheritance

# Hierachicle Inheritance mean multiple child classess inherit from one parent class

class Animal:
    def eat(self):
        print ("Animal can eat")

class Dog(Animal):
    def bark(self):
        print ("Dog barks")

class cat(Animal):
    def meow(self):
        print ("cat meow")

d = Dog()
c = cat()

d.eat()
d.bark()
c.eat()
c.meow()

# Hybrid Inheritance

# Hybrid Inheritance is a combination of multiple and different multileval inheritance.

class A:
    def show(self):
        print("class A")

class B:
    def show (self):
        print("class B")

class C(A):
    def show (self):
        print("class c")

class D(B,C):
    def display(self):
        super().show()

obj = D()

obj.display()

# super() follow MRO(Method resolution order)
# in class D(B,C)python first cheack class B.

# Type() function

# The type function returns the data type of a varriable or object.

a = 10
b = 5.5
c = "python"

print (type (a))
print (type (b))
print (type (c))

# dir() function

# The dir() function lits all atributes and methods of a class or object.

class student:

     def __init__ (self):
         self.name = "gopal"

def show (self):
        print("Studentname :",self.name)

obj = student()

print (dir(obj))

# isinstance() function

# The isinatance function cheacks weather an object belongs to a class.

class parson:
    pass

obj = parson()

print (isinstance(obj , parson))

# help () function

# The help() function display the documention string of a class or function.

class demo():

    """This is method display message"""

help (demo)

