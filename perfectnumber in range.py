for n in range(1,1001):
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum +=i
        i+=1
    if sum==n:
        print("Number is perfect",n)
         