# A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

m=eval(input("Enter your marks:"))
g=0

if (m>80):
    print("Your Grade is: A")
elif(m<25):
    print("Your Grade is: F")
elif(m>60 and m<80):
    print("Your Grade is: B")
elif(m>50 and m<60):
    print("Your Grade is: C")
elif(m>45 and m<50):
    print("Your Grade is: D")
elif(m>25 and m<45):
    print("Your Grade is: E")
else:
    print("Enter valid input (between 0-100)")