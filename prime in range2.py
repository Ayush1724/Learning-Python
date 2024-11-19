for n in range(11,101):
    t=n
    c=0
    i=2
    while i<n:
        if(n%i==0):
            c+=1
        i+=1     

    if(c==0):
        print(n,"prime")        