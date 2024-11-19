import math
def abc(a):
    c=0
    arm=0
    b=a
    while b>0:
        c+=1
        b=b//10
    b=a
    while b>0:
        r=b%10
        arm = arm + pow(r,c)
        b=b//10
    if arm == a:
        print(arm)
for i in range(1,1001):
    abc(i)               