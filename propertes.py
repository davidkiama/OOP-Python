class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


se1 = SoftwareEngineer()
se1.salary = 10000  # "setting"
print(se1.salary)  # 10000 "getting"
del se1.salary  # "deleting"
print(se1.salary)  # AttributeError: 'SoftwareEngineer' object has no attribute


# Recap:
# 1. getter and setter
# 2. getter -> @property
# 3. setter -> @x.setter
