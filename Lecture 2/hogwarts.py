students = ["Hermione", "Harry", "Ron"]

# standard way to print
print(students[0])
print(students[1])
print(students[2])

# Using loop
for student in students:
    print(student)

# Using range & len function
for i in range(len(students)):
    print(i+1, students[i])
