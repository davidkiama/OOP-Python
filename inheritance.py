
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


class Designer(Employee):
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
de1 = Designer('John', 50000)
se1 = SoftwareEngineer('Mary', 60000, 'Senior')
# print(de1)  # John earns 50000.(__str__)

# 2. Inheritance of methods
# de1.work()  # John is working as a designer...
# se1.work()  # Mary is working...

# Extending the parent class.
# 1. Entending  of properties
# print(se1.level)  # Senior. This property is only availabe in the child class.

# 2. Extending of methods
# de1.draw()  # John is drawing...
# se1.debug()  # Mary is debugging...
# A software engineer can debug but not draw.
# se1.draw()  # AttributeError: 'SoftwareEngineer' object has no attribute 'draw'


# If we use the same name for the child method, it will override the parent method.
# This is called method overriding.
# If we use diferrent name for the child method, we are extending the child class.
# se1.work()  # Mary who is a Senior engineer is working...


# POLYMORPHISM
# Polymorphism is the ability of an object to take on many forms.
# For example, an employee can be a be coding or designing.

# List of employees
employees = [
    Designer('John', 50000),
    Designer('James', 60000),
    SoftwareEngineer('Mary', 60000, 'Senior'),
    SoftwareEngineer('Steve', 70000, 'Junior'),
    SoftwareEngineer('Bill', 80000, 'Senior'),
]


def motivate_emloyees(employess):
    for employee in employees:
        employee.work()


motivate_emloyees(employees)
'''
    OUTPUT:
        John is working as a designer...
        James is working as a designer...
        Mary who is a Senior engineer is working...
        Steve who is a Junior engineer is working...
        Bill who is a Senior engineer is working...

'''

# Recap:
# 1. Inheritance ChildClass(ParentClass)
# call the super().__init__() method to call the parent class constructor.
# 2  Inheritance, Extending and Overwriting
# 3. Polymorphism
