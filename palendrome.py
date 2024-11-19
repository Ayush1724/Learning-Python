a=int(input("Enter the number :- "))
b=a
pld=0
while b>0:
    r=b%10
    pld=pld*10+r
    b=b//10
if pld==a :
    print ("Palandrome")  
else:
    print("Not a palandrome")  