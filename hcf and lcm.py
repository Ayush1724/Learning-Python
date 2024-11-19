a=int(input("Enter the number 1 :- "))
b=int(input("Enter the number 2 :- "))
hcf=0
lcm=0
for i in range(1,a+1 and b+1):
    if (a%i==0 and b%i==0):
        hcf=i
lcm=(a*b)/hcf
print("hcf is :- ",hcf)
print("lcm is :- ",lcm)
