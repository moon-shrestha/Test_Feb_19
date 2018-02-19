''' Q3. Create a Student class and initialize it with name and roll number. Make methods to :
      a. Display - It should display all informations of the student.
      b. setAge - It should assign age to student
      c. setMarks - It should assign marks to the student.
'''

class Student:

    age = 0
    marks = 0

    def __init__(self, name, roll_num):
        self.name=name
        self.roll_num=roll_num

    def Age(self, age):
        self.age=age

    def Marks(self, marks):
        self.marks = marks

    def Display(self):
        return "name:{} - roll:{} - age:{} - marks{}.".format(self.name, self.roll_num, self.age, self.marks)

s=Student("Moon", 629)
Student.Age(s,20)
print(s.name,s.roll_num)
print(s.age)

Student.Marks(s,74)
print(s.marks)

print(Student.Display(s))