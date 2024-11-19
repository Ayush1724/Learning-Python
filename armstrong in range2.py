import math
def arms(a):
    b=a
    arm=0
    cod=0
    while b>0:
        cod+=1
        b=b//10
    b=a
    while b>0:
        r=b%10
        arm=arm+pow(r,cod)
        b=b//10
    if arm==a:
        print("Armstrong numbers are :- ",arm)

for i in range(10,1000):
    arms(i)
           
