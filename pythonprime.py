a=int(input("Enter a: "))
values = range(1,a+1)
f=0
for i in values:
    if (a % i ==0):
        f=f+1
if (f==2):
    print(a,"is a prime number.")
else: print(a,"is not a prime number.")