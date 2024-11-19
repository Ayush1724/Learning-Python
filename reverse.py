n=int(input("Enter the number :- "))
r=0
a=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10

print("Reverse number is :- ",sum)
if(a==sum):
    print("palendrom")
else:
    print("not a palindrom")   