print('''
Avaliable operations:
+ ADD
- SUBSTRACT
* PRODUCT
/ DIVIDE  
''')

input1=eval(input("Enter the first value:"))
input2=input("Enter the operation:")
input3=eval(input("Enter the second value:"))
if input2== '+':
    print("The output:",(input1+input3))
elif input2=='-':
    print("The output:",(input1-input3))
elif input2=='*':
    print("The output:",(input1*input3))
elif input2=='/':
    print("The output:",(input1/input3))
else:
    print("Invalid operation")
