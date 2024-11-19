import math
def aut(a):
    s=a*a
    b=a
    cod=0
    while b>0:
        cod+=1
        b=b//10
    c=pow(10,cod)
    au=s%c
    if au==a:
        print("Automorphic :- ",a," and its sq is ",s)
for i in range(1,1000):
    aut(i)        

