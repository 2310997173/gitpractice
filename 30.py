# Assignment-5
# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Sum of first n natural numbers
# n = int(input("Enter a number: "))
# sum_n = 0
# i = 1
# while i <= n:
#     sum_n += i
#     i += 1
# print("Sum:", sum_n)

# 3. Factorial of a number
# num = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# print("Factorial:", fact)

# 4. Reverse a given number
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print("Reversed Number:", rev)

# 5. Keep taking numbers until user enters 0
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break

# 6. Stop when the user enters an even number
# while True:
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         break

# 7. Password check
# correct_password = "password123"
# while True:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Access Granted")
#         break
#     print("Access not granted")

# 8. Guess the secret number
# secret_number = 7
# while True:
#     guess = int(input("Guess the number: "))
#     if guess == secret_number:
#         print("Correct!")
#         break
#     print("Inccorect")

# 9. Count from 1 to 10 but stop at 5
# i = 1
# while i <= 10:
#     if i == 6:
#         break
#     print(i)
#     i += 1

# 10. Print only odd numbers from 1 to 10 using continue
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 11. Print numbers from 1 to 10 but skip 5
# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 12. Print only positive numbers, skip negatives
# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         continue
#     print("Positive Number:", num)
#     break

# 13. Print numbers from 1 to 20 but skip multiples of 3
# i = 1
# while i <= 20:
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 14. Keep asking for a number but skip odd numbers until an even number is entered
# while True:
#     num = int(input("Enter a number: "))
#     if num % 2 == 1:
#         continue
#     break