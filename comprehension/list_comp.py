# List of student scores
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]

#one
# This filters out all scores that are 60 or below in a new list 'passed'
passed = [x for x in scores if x > 60]
print(passed)  # Output: [78, 88, 90, 62, 99, 70]

#two
# Create a new list 'result' that labels each score as 'Pass' if it's greater than 50, otherwise 'Fail'
result = ["Pass" if score > 50 else "Fail" for score in scores]
print(result)  # Output: ['Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']


