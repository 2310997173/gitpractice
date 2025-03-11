# 6.find out the grades based on the user score the grade should be assign as follows:90 above : a , 70-89 b,50-69 c and below 50 f
marks = int(input("enter the grade: "))
if(marks>=90):
    print("Grade: A")
elif(marks>=70):
    print("Grade: B")
elif(marks>=50):
    print("Grade: c")
else:
    print("Grade: F")
    