def per(a):
    sum=0
    i=1
    while i<a:
        if a%i==0:
            sum+=i
        i+=1
    if sum==a:
        print ("Perfect number :- ",sum)
for i in range(1,1001):
    per(i)            