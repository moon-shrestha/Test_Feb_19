''' Define an employee class and initialize it with name and salary. Now, make a classmethod that takes
 a string parameter "name-2000" which creates an instance and returns the instance based on parameter.'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name

    @classmethod

    def getObjFromString(cls, inp):
        name, salary = inp.split("-")
        return cls(name, salary)

e=Employee.getObjFromString("Max-2000")
print(e.__dict__)
