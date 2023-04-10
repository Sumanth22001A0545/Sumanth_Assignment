a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("1-addition\t\t2-subtraction\n3-multiplication\t\t4-division")
m=int(input("Enter the number according to the operation required: "))
if (m==1):
    c=a+b
elif (m==2):
    c=a-b
elif (m==3):
    c=a*b
elif (m==4):
    c=a/b
else :
    print("Invalid number entered.Please try again")
print("The result is",c)