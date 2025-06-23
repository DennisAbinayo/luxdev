# CONTROL FLOWS

# Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Check if someone is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Print the largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is {largest}.")

# Practice combining and, or, not
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))

## and
if x > 0 and y > 0:
    print("Both x and y are positive.")
else:
    print("At least one of x or y is not positive.")

## or
if x == 0 or y == 0 or z == 0:
    print("At least one of x, y, or z is zero.")
else:
    print("None of x, y, or z is zero.")

## not
if not (x < 0):
    print("x is not negative.")
else:
    print("x is negative.")

# Challenge

# Grading System
score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
