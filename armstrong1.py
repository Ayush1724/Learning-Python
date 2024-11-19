import math
n= int(input("Enter the number :- "))
t=n
c=0
arm=0
while t>0:
    c+=1
    t=t//10
t=n
while t>0:
    r=t%10
    arm=arm+pow(r,c)
    t=t//10
if arm==n:
    print("armstrong number ",arm)
else:
    print("Not a armstrong number ",arm)       