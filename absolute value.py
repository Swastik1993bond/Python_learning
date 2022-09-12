#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1  x=-5, |x|=5
#INPUT: -1        OUTPUT: 1

from math import sqrt
num=eval(input("Enter the number:"))
abs=sqrt(num**2)
print(float(abs),"is the absolute value")