def my_function(a,b,*age,c = 0,d = 0,**keyword):
    print("Postional assignment: ",a,b)
    print("Extra Postional argument: ",age)
    print("Keyword argument: ",c,d)
    print("Extra kewyword are: ",keyword)

    total = a+b+c+d
    total = total+sum(age)
    print(total)
my_function(10,20,30,40,c = 5,d = 10,
            fname = "Ram",lname = "Sharma")