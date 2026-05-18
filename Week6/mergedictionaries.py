# Developing a script to be able to merge following dictionaries:
# with the conditon of name value with "ex" pattern 

# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 20,
    "course" : "Computer Science",
    "city": "Auckland",
    "status": "lecturer"
}

# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}
 
# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

# putting all dictionaries in a list
students = [student1, student2, student3]

# create an empty dictionary to store merged data
merged_students = []

# check if name contains "ex" pattern and merge dictionaries
for student in students:
    if "ex" in student["name"].lower():
        merged_students.append(student)

# display merged dictionaries
print("student with 'ex' pattern in name:")
for student in merged_students:
    print(student)