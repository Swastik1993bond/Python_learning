#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
# Judge and print total cost for user.

d=0
q=int(input("Enter the quantity of order,(Cost of one unit is 100):"))
tc=0
if(q>1000):
    d=0.1
    tc= 100*(1-d)*q
    print("your total cost is: ",tc)
elif(q<0):
    print("Enter a valid Input(Non-zero)")
else:
    tc= 100*q
    print("your total cost is: ",tc)

