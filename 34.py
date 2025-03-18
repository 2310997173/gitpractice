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
myfamily = {
    "child1" : {
        "Name" : "Ram",
        "Age" : 20
    },
    "child2" : {
        "Name" : "Lucky",
        "Age" : 25
    },
    "child3" : {
        "Name" : "Ash",
        "Age" : 18
    },
}
print(myfamily["child2"]["Name"])

# 
student1={}
for _ in range(10):
    roll_no = input["Enter the roll no: "]