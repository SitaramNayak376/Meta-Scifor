#qs1

class Student:
  def __init__(self,roll_no,name,age,grade):
    self.roll_no=roll_no
    self.name=name
    self.age=age
    self.grade=grade
class StudentManagementSystem:
  def __init__self(self):
    self.student =[]
  def accept_student_details(self):
    roll_no=input("enter roll no:")
    name=input("enter name:")
    age=input("enter age:")
    grade=input("enter grade:")
    student=Student(roll_no,name,age,grade)
    self.student.append(student)
    print("student added successfully.\n")

  def display_student_details(self):
    if not self.students:
      print("no student details available.\n")
      return
    for student in self.students:
      self.print_student_details(student)
  def search_student_details(self):
    roll_no = input("enter roll no to search:")
    for student in self.students:
      if student.roll_no==roll_no:
        self.print_student_details(student)
        return
    print("Student not found.\n")

  def update_student_details(self):
    roll_no = input("enter roll no to update")
    for student in self.students:
      if student.roll_no==roll_no:
        student.name=input("enter new name:")
        student.age=input("enter new age:")
        student.grade=input("enter new grade:")
        print("student details updated successfully.\n")
        return
    print("student not found.\n")

  def print_student_details(self,student):
    print("roll no:", student.roll_no)
    print("name:", student.name)
    print("age:", student.age)
    print("grade:", student.grade)
    print()

  def menu(self):
    while True:
      print("1.accept student details")
      print("2.display student details")
      print("3.search details of a student")
      print("4.delete details of a student")
      print("5.update student details")
      print("6.exit")
      choice = input("enter your choice:")

      if choice=='1':
        self.accept_student_details()
      elif choice=='2':
        self.display_student_details()
      elif choice=='3':
        self.search_student_details()
      elif choice=='4':
        self.delete_student_details()
      elif choice =='5':
        self.update_student_details()
      elif choice=='6':
        print("exit the program.")
        break
      else:
        print("invalid choice")

if __name__ == "__main__":
  sms = StudentManagementSystem()
  sms.menu()