#question : A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

yos=eval(input("Enter your year of Service:"))
bon=0
fsal=0
sal=eval(input("enter your Salary:"))
if (yos>=5):
    bon =0.05
    print("The bonus is:",(sal*bon))
else:
    print("The bonus is: 0")

