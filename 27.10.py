class NameSurname:
   def __init__(self,name, surname):
    self.name = name
    self.surname = surname
class Student:
   student_amout = 0
   def __init__(self,name, surname,age, height=129):
       self.ns  = NameSurname(name,surname)
       self.age = age
       self.height = height
       Student.student_amout += 1
   def printStudent(self):
       print(f'Name:{self.ns.name}')
       print(f'Surname:{self.ns.surname}')
       print(f'Age:{self.age}')
       print(f'Height:{self.height}')

print(f'before creating Student objekt{Student.student_amout}')
first_student = Student( "misha", "morvaniuk", 11)
first_student.printStudent()
print(f'before creating Student objekt1{first_student.student_amout}')

