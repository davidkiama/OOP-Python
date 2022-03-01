
# class
class SoftwareEngineer:

    # class attribute
    language = "Python"

    def __init__(self, name, age, level, salary):
        # instance attributes - Each instance of the class will have these attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance
software_engineer = SoftwareEngineer('John', 30, 'Senior', 100000)
print(software_engineer.level, software_engineer.salary)  # Senior 100000


# we CAN'T access the INSTANCE attributes directly
# print(SoftwareEngineer.name) # AttributeError: 'SoftwareEngineer' object has no attribute 'name'

# we can access the CLASS attributes directly
# print(SoftwareEngineer.language)  # Python
# print(software_engineer.language)  # Python

# Recap:
# 1. Class attributes are shared by all instances of the class
# 2. Instance attributes are unique to each instance of the class
# 3. Instance attributes are defined in the __init__ method
