# def name(fname,lname):
#     print("The youngest child name is: ",fname+" "+lname)
# c = name("Ram")
# print(c)

def name(*kids):
    print("The child name is: ",kids[2])
c = name("Ram","Sita","Sham")
print(c)    