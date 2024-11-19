a= int(input("Enter the digit :- "))
sum=0
b=a
while b>0:
    r=b%10
    sum = sum +r
    b=b//10

print("sum of digit is :- ",sum)    