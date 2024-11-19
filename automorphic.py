import math
cod=0
a=int(input("Enter the number :- "))
b=a
s=a*a
while b>0:
    cod +=1
    b=b//10
c=pow(10,cod)
aw=s%c
if aw==a:
    print("Automorphic")
else:
    print("Not a automorphic")    