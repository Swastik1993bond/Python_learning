# i=2
# print(i)

#print("hello")

#for i in range(1, 11):
 #   print(i)

#L= [1,2,4,5,6,9,3,45,21,27]
#T=(1,2,4,5,6,9,3,45,21,27)

#print(L,type(L))
#print(T,type(T))

#x=10
#y=20
#z=30
#print("Binary value of x is :",bin(x))
#print("Binary value of y is :",bin(y))
#print("Binary value of z is :",bin(z))

#print("Octal value of x is :",oct(x))
#print("Octal value of y is :",oct(y))
#print("Octal value of z is :",oct(z))

#print("binary of x&y:",bin(x&y))
#print("binary of x or y:",bin(x|y))
#print("binary of x x-or y:",bin(x^y))

#print(type(x))
#a=1
#print(type(a))
#b=2.5
#print(type(b))
#c=2+5j
#print(type(c))
#d= "Marry had a little lam"
#print(type(d))

#d= {
#    'name':'Swastik',
#    'age':'28'
#    }
#print(d,type(d))


#set = immutable

#my_set={1,2,3,1}
#print(my_set)
#print(type(my_set))

# set WILL REMOVE DUPLIACTE ELEMENTS

#typecasting and user input = input(),int(),float(),eval()

#a=input("Enter A value:")
#b=input("Enter another value:")
#print(a+b)

#typecasting for int:

#a=int(input("Enter A value:"))
#b=int(input("Enter another value:"))
#print(a+b)

#typecasting for float:

#a=float(input("Enter A value:"))
#b=float(input("Enter another value:"))
#print(a+b)

#If-else:

#a=10
#if a%2 ==0:
#    print(a,"is Even number")
#else :
#    print(a,"is odd number")


#a=123
#r=0
#while(a!=0):
#    i=a%10
#    r=r*10+i
#    a/=10   
#print(r)
#else :
#    print(a,"is odd number")

#for n in range(10,1,-2):
#    print(n)

#i=10
#while i>=1:
#   i-=1
#    print ('Welcome',i,'th')

#string handling 
#w= "I am Swastik Mukherjee"
#print(w[6])
#print(w[-3])

# to slice multiple value:
#print(w[1:8])
#rint(w[4:-1])

#giving increment:
#print(w[::1]) #print exact
#print(w[::-1])  # for reversing the string
#print(w[-1:-10:-1])
#print(w[-4::-2]) #from a particular starting point

#iteration of string:
w= "I am Swastik Mukherjee"
t=len(w)
#print(t)
for a in range(t):
    print(w[0:a+1])