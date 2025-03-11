# # Assignment-3
# Program for basic arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# # Program to find the average of three numbers
# a = 10
# b = 20
# c = 30
# average = (a + b + c) / 3
# print("Average:", average)

# # Program to find the average of three numbers by taking input values
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# average = (a + b + c) / 3
# print("Average:", average)

# # Program to calculate simple interest
# p = float(input("Enter principal amount: "))
# r = float(input("Enter rate of interest: "))
# t = float(input("Enter time in years: "))
# simple_interest = (p * r * t) / 100
# print("Simple Interest:", simple_interest)

# # Program to calculate compound interest
# p = float(input("Enter principal amount: "))
# r = float(input("Enter rate of interest: "))
# t = float(input("Enter time in years: "))

# compound_interest = p * ((1 + r / 100) ** t)
# print("Compound Interest:", compound_interest)


# # Program to find the square root
# num = float(input("Enter a number: "))
# print("Square Root:", num ** 0.5)

# # Program to find the area of a circle
# radius = float(input("Enter radius: "))
# print("Area of Circle:", 3.1416 * radius ** 2)

# # Program to find the area of a rectangle
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))
# print("Area of Rectangle:", length * breadth)

# # Program to find the area of a right-angled triangle
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
# print("Area of Right-Angle Triangle:", 0.5 * base * height)

# # Program to swap two variables using a temporary variable
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# temp = a
# a = b
# b = temp
# print("Swapped values:", a, b)

# # Program to convert Fahrenheit to Celsius
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5 / 9
# print("Temperature in Celsius:", celsius)

# # Program to display a calendar
# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# print(calendar.month(year, month))

# # Program to convert days into years, weeks, and days
# days = int(input("Enter number of days: "))
# years = days // 365
# weeks = (days % 365) // 7
# days_remaining = (days % 365) % 7
# print(f"{years} Years, {weeks} Weeks, {days_remaining} Days")