# Assignment-6
# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# # 2. Print only even numbers from 1 to 20
# for i in range(2, 21, 2):
#     print(i)

# # 3. Print the multiplication table of 5
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")

# # 4. Sum of the first n natural numbers
# n = int(input("Enter a number: "))
# sum_n = sum(range(1, n + 1))
# print("Sum:", sum_n)

# # 5. Reverse a string using a for loop
# string = input("Enter a string: ")
# reversed_string = ""
# for char in string:
#     reversed_string = char + reversed_string
# print("Reversed String:", reversed_string)

# # 6. Count the number of vowels in a string
# string = input("Enter a string: ").lower()
# vowel_count = sum(1 for char in string if char in "aeiou")
# print("Number of vowels:", vowel_count)

# # 7. Print each element of a list
# lst = [10, 20, 30, 40, 50]
# for item in lst:
#     print(item)

# # 8. Find factorial of a number
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial:", fact)

# # 9. Find the largest number in a list
# numbers = [10, 50, 30, 90, 70]
# largest = max(numbers)
# print("Largest number:", largest)

# # 10. Print numbers 1 to 10, but stop at 5
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# # 11. Find and print the first even number from a list, then stop
# numbers = [1, 3, 5, 7, 8, 9]
# for num in numbers:
#     if num % 2 == 0:
#         print("First even number:", num)
#         break

# # 12. Find first occurrence of 'a' in a word and stop
# word = input("Enter a word: ")
# for index, char in enumerate(word):
#     if char == 'a':
#         print("First 'a' found at index:", index)
#         break

# # 13. Ask for a password until correct one is entered
# correct_password = "python123"
# while True:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Access granted!")
#         break

# # 14. Print multiplication table of 7 but stop at 7 × 5
# for i in range(1, 11):
#     if i > 5:
#         break
#     print(f"7 x {i} = {7 * i}")

# # 15. Print numbers from 1 to 10 but skip 5
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# # 16. Print only odd numbers from 1 to 10
# for i in range(1, 11, 2):
#     print(i)

# # 17. Print multiplication table of 3 but skip multiples of 6
# for i in range(1, 11):
#     if (3 * i) % 6 == 0:
#         continue
#     print(f"3 x {i} = {3 * i}")

# # 18. Print only consonants in a word
# word = input("Enter a word: ")
# for char in word:
#     if char.lower() in "aeiou":
#         continue
#     print(char, end="")

# # 19. Print only positive numbers from a list
# numbers = [-10, 5, -3, 8, -1, 7]
# for num in numbers:
#     if num < 0:
#         continue
#     print(num)

# # 20. Print numbers from 1 to 20 but skip numbers divisible by 4
# for i in range(1, 21):
#     if i % 4 == 0:
#         continue
#     print(i)

# # 21. Print multiplication table from 1 to 5 using nested loops
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()
