a= int(input("Enter the number :- "))
b=a
sum=0
mul=1
while b>0:
    r=b%10
    sum=sum+r
    b=b//10
b=a
while b>0:
    r=b%10
    mul= mul*r
    b=b//10
if sum==mul:
    print("Spy number")
else:
    print("Not a spy number")        