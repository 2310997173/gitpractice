# cho experiments(done on date:11feb.2025)git 
# 15
# student = ["a","b","c","d","e","f","g","h","i","j","k","l"]
# SV = int(input("enter the start value: "))
# EV = int(input("enter the end value: "))
# slicing = student[2:5]
# lengthname = [len(x) for x in slicing]
# print(slicing)
# print(lengthname)

# 16
# matrix = [["1,2,3,4"],["5,6,7"],["2,4,8"]]
# print = ("Product of row: ")
# for x in matrix:
#     product = x[0]*x[1]*x[2]
# print(product)
# print = ("Product of column: ")
# for y in range(3):
#     p = matrix[0][y]*matrix[1][y]*matrix[2][y]
# print(p)

# 16(By gpt)
# matrix = [[1, 2, 3, 4], [5, 6, 7], [2, 4, 8]]

# Product of each row
# print("Product of each row:")
# for row in matrix:
#     product = 1
#     for num in row:
#         product *= num
#     print(product)

# # Finding the maximum column length to prevent index errors
# max_columns = max(len(row) for row in matrix)

# # Product of each column
# print("Product of each column:")
# for col in range(max_columns):
#     product = 1
#     valid_column = True  # To check if the column exists in all rows
#     for row in matrix:
#         if col < len(row):  # Check if column index exists in row
#             product *= row[col]
#         else:
#             valid_column = False
#             break  # Skip invalid columns
#     if valid_column:
#         print(product)

# 17
import math
raw_list = list(range(1,11))
sq_list = [y*y for y in raw_list]
fact_list = [math.factorial(x) for x in raw_list]
print(raw_list)
print(sq_list)
print(fact_list)
