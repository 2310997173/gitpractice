# 7.if student passes exam his score is above 50 or attendance is 75% attendance in the class he will promoted to next class
# score = input("enter your score: ").lower()=="yes"
# attendance = int(input("enter your attendance: "))
# if(score>50 or attendance>75):
#     print("You are passed!")
# else:
#     print("You are failed!")

# Assignment-4
# 10.Program to check if a user's login attempt is valid

# Predefined correct username and password
# correct_username = "admin"
# correct_password = "password123"

# # Taking user input
# username = input("Enter username: ")
# password = input("Enter password: ")

# # Checking login attempt
# if username == correct_username:
#     print("Login successful!")
# elif password == correct_password:
#     print("Login successful!")
# else:
#     print("Login failed! Incorrect username or password.")

# # Program to classify student's grade
# score = int(input("Enter the student's score: "))
# if 90 <= score <= 100:
#     print("Excellent")
# elif 70 <= score <= 89:
#     print("Good")
# elif 50 <= score <= 69:
#     print("Average")
# else:
#     print("Fail")

# # Program to check voting eligibility
# age = int(input("Enter age: "))
# citizen = input("Are you a citizen? (yes/no): ").lower()
# if age >= 18 and citizen == "yes":
#     print("Eligible to vote.")
# else:
#     print("Not eligible to vote.")

# # Program to check discount eligibility
# member = input("Are you a member? (yes/no): ").lower()
# total_purchase = float(input("Enter total purchase amount: "))
# if member == "yes" and total_purchase > 200:
#     print("You get a premium discount!")
# elif member == "yes" or total_purchase > 100:
#     print("You get a discount!")
# else:
#     print("No discount available.")

# # Program to check driver's license eligibility
# age = int(input("Enter age: "))
# driving_test_passed = input("Did you pass the driving test? (yes/no): ").lower()
# if age >= 18 and driving_test_passed == "yes":
#     print("Eligible for a driver's license.")
# else:
#     print("Not eligible for a driver's license.")

# # Program to determine movie ticket price
# age = int(input("Enter your age: "))
# time = int(input("Enter movie time (24-hour format): "))
# base_price = 10
# if age < 12 or age > 60:
#     base_price *= 0.8  # 20% discount
# if 18 <= time <= 21:
#     base_price *= 1.1  # 10% increase
# print(f"Your ticket price is: ${base_price:.2f}")
