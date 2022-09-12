#Take input of age of 3 people by user and determine oldest and youngest among them.
print ("Enter age of 1st person")
a=input()
print ("Enter age of 2nd person")
b=input()
print ("Enter age of 3rd person")
c=input()

if (a>=b and a>=c):
    print ("1st person is oldest")
elif (b>=a and b>=c):
    print ("2nd person is oldest")
elif (c>=a and c>=b):
    print ("3rd person is oldest")
else:
    print("All are same age")