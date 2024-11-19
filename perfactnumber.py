n=int(input("Enter the number :- "))
sum=0
i=1
while i<n:
    if n%i==0:
        sum +=i
    i+=1
if sum==n:
    print("Number is perfect")
else:
    print("Not perfect number")      