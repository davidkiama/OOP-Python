import datetime


class SoftwareEngineer:

    # class attribute
    language = "Python"

    def __init__(self, name, age, level, salary):
        # instance attributes - Each instance of the class will have these attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is coding {SoftwareEngineer.language}")

    def year_born(self):
        today = str(datetime. date. today())
        curr_year = int(today[:4])
        return curr_year - self.age

    # Dunder method
    def __str__(self):
        '''
        Will be executed when you print the object
        '''
        return f"{self.name} is a {self.level} engineer with an annual salary of ${self.salary}"

    def __eq__(self, other):
        '''
        Will be executed when you compare two objects
        We will test is the name, age and level are the same
        '''
        return self.name == other.name and self.age == other.age and self.level == other.level

    # without the self parameter
    @staticmethod
    def entry_salary(age):
        '''
        WITHOUT THE DECORATOR
        We can only this as a class method but not as an instance method 
        because we need to pass the self parameter

        #WITH THE DECORATOR
        We can this as an instance method and as a class method

        However, we can't access the instance attributes eg:
            self.name...
        '''
        if age < 30:
            return 40000
        else:
            return 50000


# Create an instance of the class
steve = SoftwareEngineer("Steve", 30, "Senior", 100000)
# steve.code()  # Steve is coding Python

# retun from instance method
# print(f"Steve was born in {steve.year_born()}")  # Steve was born in 1992


# BEFORE THE __str__() METHOD
# print(steve)  # <__main__.SoftwareEngineer object at 0x7fde49cbca60>

# AFTER THE __str__() METHOD
# print(str(steve))  # Steve is a Senior engineer with an annual salary of $100000


# BEFORE THE __eq__() METHOD
# Testing equality of objects whose properties are the same
se1 = SoftwareEngineer("Steve", 30, "Senior", 100000)
se2 = SoftwareEngineer("Steve", 30, "Senior", 100000)
# print(se1 == se2)  # False Since we are comparing the location address of the objects

# AFTER THE __eq__() METHOD
# True Since we are comparing the properties (in the __eq__ method) of the objects
# print(se1 == se2)


# WITHOUT THE DECORATOR
print(SoftwareEngineer.entry_salary(25))  # 40000
# TypeError: entry_salary() takes 1 positional argument but 2 were given
print(steve.entry_salary(35))

# WITH THE DECORATOR
# print(SoftwareEngineer.entry_salary(25))  # 40000
print(steve.entry_salary(35))  # 50000


# Recap:
# 1. Class attributes are shared by all instances of the class
# 2. Special "Dunder" methods are used to override the default behavior of the object
# 3. @staticmethod is used to define a method that is not associated with any instance of the class
