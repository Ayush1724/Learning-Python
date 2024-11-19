a=int(input("Enter the number :- "))
r=0
d=0
p=1
b=a
while a>0:
    r=a%10
    if r==0:
        r+=1
    d+=r*p
    p*=10
    a=a//10
print(d)        