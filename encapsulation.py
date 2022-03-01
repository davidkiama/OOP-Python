# Encapsulation is the mechanism of hiding of data implementation.
class SoftwareEngineer:
    def __init__(self, name, level):
        self.name = name
        self.level = level

        # PROTECTED ATTIBUTES. Single underscore
        # we should access the below attributes from the outside
        # we still can but we should NOT
        self._salary = None
        self._num_of_bugs_solved = 0

        # PRIVATE ATTRIBUTES. Have double underscore
        # self.__salary = salary CANNOT BE ACCESSED FROM OUTSIDE

    def code(self):
        self._num_of_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
        # we can chek value, enforce constraints.

    # protected method
    def _calculate_salary(self, base_value):
        if self._num_of_bugs_solved < 10:
            return base_value
        elif self._num_of_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se1 = SoftwareEngineer("John", "Senior")
# se1.set_salary(3000)
# print(se1.get_salary())  # 3000


# Implementations of Encapsulation and Abstraction

# AFTER THE PROTECTED METHOD _calculate_salary
se1.code()
se1.set_salary(3000)
print(se1.get_salary())  # 3000

for i in range(10):
    se1.code()

se1.set_salary(3000)
print(se1.get_salary())  # 6000

for i in range(100):
    se1.code()

se1.set_salary(3000)
print(se1.get_salary())  # 9000


# Recap:
# 1. Encapsulation is the mechanism of hiding of data implementation .
# 2 Protected attributes (single underscore) are accessible from the outside. But we should NOT access them.
# 3 Private attributes (double underscore) are NOT accessible from the outside.
