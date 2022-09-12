#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

#Modify the above question to allow student to sit if he/she has medical cause. 
#Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

cls=int(input("How many classes? " ))
atn=int(input("Number of classes attended:"))
med=input("Do you have any medical cause?(Y/N) ")
par=float(atn/cls)
if ( med=='Y' or med == 'y'):
    print ("allowed to sit in exam")
elif atn>0 and cls>0 :
    if par>0.75:
        print ("allowed to sit in exam")
    else:
        print("Not allowed to sit in exam")
else:
    print("Enter valid Inputs (Non-Zero)")
