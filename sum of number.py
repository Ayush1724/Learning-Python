x=1
n=int(input("Enter the number :- "))
sum=0

while n>0:
    r=n%10
    sum+=r
    n=n//10
    
print(sum)
