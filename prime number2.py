n= int(input("Enter the number :- "))
a=2
c=0
while a<n:
    if n%a==0:
        c+=1
    a+=1
if c==0:
    print("Prime number")      
else:
    print("Not a prime number")  

