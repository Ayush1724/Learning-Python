import math
def arms(a):
    arm=0
    c=0
    b=a
    while b>0:
        c +=1
        b=b//10
    b=a
    while b>0:
        r=b%10
        arm=arm+pow(r,c)
        b=b//10
    if arm==a:
        print("Armstrong number :- ",a)

for i in range(10,1000):
    arms(i)        

