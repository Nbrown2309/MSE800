# Adding in class so student can get the following information
class Student: 
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id


# Function 1: Collecting Following Data
def collect_students():
    students = [] # local variable (only used inside this function)

    for i in range(3):
        print(f"\nEnter Details for student {i+1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        student_id = input("Student ID: ")

        student = Student(name, age, student_id) # create an object
        students.append(student) #adds to list

    return students

# Function 2: Display students names and age
def display_students(students):
    print("\nStudents Names & Ages: ")

    #sort students by age (small to large)
    students.sort(key = lambda x: x.age)

    for student in students:
        print(student.name, "-", student.age)

#main program
student_list = collect_students() # call function to collect data
display_students(student_list) # call function to display data