# A list of students and their respective marks
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]


#one
# pairs each student with their mark in a dictionary
# zip() function takes multiple iterables like lists and aggregates elements from each. Generates an iterator of tuples
# in this case zip(students, marks) will produce >>> ('Alice', 82), ('Bob', 48), ('Charlie', 79), ('Diana', 65), ('Eve', 91)

student_details = {
    student : mark for student, mark in zip(students, marks)
}

print(student_details)


#two
#dictionary that stores only students who scored more than 70

result={
    student : mark for student, mark in zip(students, marks) if mark > 70
}

print(result)


#three
#dictionary that maps each student to "Pass" or "Fail" (threshold: 50)

pass_or_fail = {
    student : 'Pass' if mark > 50 else 'Fail' for student, mark in zip(students, marks)
}

print(pass_or_fail)