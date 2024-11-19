a=int(input("Enter the number :- "))
r=0
rev=0
b=a
for a in range(1,n):
    r=a%10
    rev=rev*10+r
    a=a//10

print(rev)
print(r)
print(a)
