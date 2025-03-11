# 9.if a customer is eligible for discount , the customer is eligible for discount if he/she is the member or there purchase is over 1000 rs 
member = input("Are you member of our store?: ").lower()=="yes"
purchase = int(input("enter the amount: "))
if(member or purchase>1000):
    print("You get a discount!")
else:
    print("Discount unavailable")