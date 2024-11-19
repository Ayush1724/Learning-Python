a=int(input("Enter the number :- "))
b=1
c=0
while(b<=a):
    if a%b==0:
        c+=1
    b+=1    
if c==2:
    print("prime number")  
else:
    print("Not a prime number")      
