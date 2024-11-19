a=int(input("Enter the number :- "))
rev=0
r=0
for i in range(1,len(str(a))+1):
    r=a%10
    rev=rev*10+r
    a=a//10

print(rev)    
