n=int(input("Enter the number :- "))
r=0
rev=0
a=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
    
print("Rev no. is ",rev)
c=a-rev
if c>0:
    print("The difference b/t numbers is ",c)
else:
    print("The difference b/t numbers is ",c*-1)    