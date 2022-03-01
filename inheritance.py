
'''
Inheritance- when a class inherits from another class, 
it gains all the properties and methods of the parent class.

We can inherit, extend and overwrite the properties and methods of a parent class.
'''


class Employee:
    '''
    This is the base class or the parent class
    '''

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is working...")


class Desginer(Employee):
    '''
    This is the child class or the derived class
    '''

    def __str__(self):
        return f'{self.name} earns {self.salary}'

    def draw(self):
        print(self.name, "is drawing...")

    def work(self):
        print(self.name, "is working as a designer...")


class SoftwareEngineer(Employee):
    '''
    This is the child class or the derived class
    '''

    def __init__(self, name, salary, level):

        # EXTENDING THE PARENT CLASS
        super().__init__(name, salary)
        self.level = level

    def debug(self):
        print(self.name, "is debugging...")

    def work(self):
        print(f'{self.name} who is a {self.level} engineer is working...')


# INHERITANCE
# 1. Inheritance of attributes
de1 = Desginer('John', 50000)
se1 = SoftwareEngineer('Mary', 60000, 'Senior')
# print(de1)  # John earns 50000.(__str__)

# 2. Inheritance of methods
# de1.work()  # John is working...
# se1.work()  # Mary is working...

# Extending the parent class.
# 1. Entending  of properties
print(se1.level)  # Senior. This property is only availabe in the child class.

# 2. Extending of methods
# de1.draw()  # John is drawing...
# se1.debug()  # Mary is debugging...
# A software engineer can debug but not draw.
# se1.draw()  # AttributeError: 'SoftwareEngineer' object has no attribute 'draw'


# If we use the same name for the child method, it will override the parent method.
# This is called method overriding.
# If we use diferrent name for the child method, we are extending the child class.
se1.work()  # Mary who is a Senior engineer is working...
