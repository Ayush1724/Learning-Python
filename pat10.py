n=int(input("Enter the number"))
for t in range(1,2*n):
    print("0",end=" ")
print()    
for i in range(1,n+1):
    for s in range(1,(n-i)+1):
        print("0",end=" ")
    for j in range(1,(2*i)):
         print(" ",end=" ")
    for s in range(1,(n-i)+1):
        print("0",end=" ")     
    print()     