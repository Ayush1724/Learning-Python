n=int(input("Enter the number"))
for i in range(1,n+1):
    for s in range(1,i):
        print(" ",end=" ")
    for j in range(1,n-i+2):
         print("*",end=" ")
    print()     