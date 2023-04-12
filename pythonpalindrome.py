a=int(input("Enter thee number: "))
i=0
while(a>0):
    digit=a%10
    i=i+1
    a=a/10

print(i)