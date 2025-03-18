carinfgo = {
    "brand" : "Tata",
    "year" : 1998,
    "color" : ["white","red","orange"]
}

# carinfgo.pop("brand")
# carinfgo.popitem()
# del carinfgo["color"]
# del carinfgo
# carinfgo.clear()
# print(carinfgo)

# car = carinfgo.copy()
# car1 = dict(carinfgo)
# print(car)
# print(car1)

# for x in carinfgo:
    # print(x)   method to keys of dictinory 

# for x in carinfgo.keys():
#     print(x)  method to keys of dictinory

# for x in carinfgo.values():
#     print(x)  method to get values of dictinory

# for x,y in carinfgo.items():
#     print(x,y)

# nested dictinory 
# myfamily = {
#     "child1" : {
#         "Name" : "Ram",
#         "Age" : 20
#     },
#     "child2" : {
#         "Name" : "Lucky",
#         "Age" : 25
#     },
#     "child3" : {
#         "Name" : "Ash",
#         "Age" : 18
#     },
# }
# print(myfamily["child2"]["Name"])

# 
student1={}
for _ in range(6):
    roll_no = input("Enter the roll no: ")
    student1[roll_no] = {
        "Name" : input("Enter the name: "),
        "Age" : input("Enter the age: "),
        "Course" : input("Enter your course: "),
        "Block" : input("Enter your block name: ")
    }
    print("Student data is added")

Search_roll_no = input("Enter the roll no you want to search: ")
if Search_roll_no in student1:
    print("Student Details")
    print("Name: ",student1[Search_roll_no]["Name"])
    print("Age: ",student1[Search_roll_no]["Age"])
    print("Course: ",student1[Search_roll_no]["Course"])
    print("Block: ",student1[Search_roll_no]["Block"])
else:
    print("Record not found!")    