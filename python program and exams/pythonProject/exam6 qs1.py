class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            student = Student(student_id, name, age, grade)
            self.students[student_id] = student
            print("Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print("Student details updated successfully.")
        else:
            print("Student not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Accept Student Details")
        print("2. Display Student Details")
        print("3. Search Details of a Student")
        print("4. Delete Details of Student")
        print("5. Update Student Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            system.add_student(student_id, name, age, grade)

        elif choice == '2':
            system.display_students()

        elif choice == '3':
            student_id = input("Enter Student ID to search: ")
            system.search_student(student_id)

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            system.delete_student(student_id)

        elif choice == '5':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            age_input = input("Enter new Age (leave blank to keep current): ")
            age = int(age_input) if age_input else None
            grade = input("Enter new Grade (leave blank to keep current): ")
            system.update_student(student_id, name if name else None, age, grade if grade else None)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
