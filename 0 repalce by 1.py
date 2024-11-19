a= int(input("Enter the number :- "))
b=a
r=0
p=1
d=0
while b>0:
    r=b%10
    if r==0:
        r=r+1
    d +=r*p
    p *=10
    b=b//10

print("Replacing all the zero ",d)    