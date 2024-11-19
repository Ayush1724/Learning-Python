n=5
mid=(n+1)/2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==mid or j==mid or i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    