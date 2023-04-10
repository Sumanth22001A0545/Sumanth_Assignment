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
if (max==a):
    if (b<c):
        min=b
elif (max==b):
    if(a<c):
        min=a
elif (max==c):
    if(a<b):
        min=a
print("The minimum value is",min)
