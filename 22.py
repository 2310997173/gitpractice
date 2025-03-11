# 4.find largest of three numbers provided by user
n1 = int(input("enter the no: "))
n2 = int(input("enter the no: "))        
n3 = int(input("enter the no: "))
if(n1>n2 and n3<n1):
    print("Num1 is the largest")
elif(n2>n3 and n1<n2):
    print("Num2 is the largest")
elif(n3>n2 and n2<n3):
    print("Num3 is the largest")
else:
    print("Invalid choice!")