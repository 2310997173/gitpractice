def fact(n):
    if n==0 or n==1:
        return 1
    else :
        return n*fact(n-1)
n = int(input("Enter the no: "))
if n<0:
    print("NEgative are not allowed!")
else:
    result = fact(n)
    print(f"Factortrial of{n} is: {result}")