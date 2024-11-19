import math
a=int(input("Enter the number :- "))
arm=0
b=a
c=0
while b>0:
    c =c+1
    b=b//10
    
b=a    
while b>0:
    r=b%10
    arm=arm+pow(r,c)
    b=b//10

if arm==a:
    print("Armstrong")
else:
    print("Not a armstrong")    


    