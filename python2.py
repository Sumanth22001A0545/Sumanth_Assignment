a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if (a>b and a>c):
    max=a
elif(b>c):
    max=b
else : 
    max=c
print("The maximum value is",max)
