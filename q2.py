'''Q2. Create a class Circle which has a class variable PI with value=22/7. Make two methods getArea and
getCircumference inside this Circle class. Which when invoked returns area and circumference of each ciecle instances.
'''

class Circle:

    PI = 22/7


    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return self.radius*self.radius*2*Circle.PI

    def getCircumference(self):
        return self.radius*2*Circle.PI

c=Circle(7)
print(c.getArea())
print(c.getCircumference())
