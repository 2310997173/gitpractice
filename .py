class person:
    def __init__(abc, name, age):
        abc.name = name
        abc.age = age
    def greeting(abc):
        print("Hello, My name is "+abc.name)
p1 = person('Ram', 24)
p1.greeting()
print(p1.name)

