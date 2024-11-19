def prm(a):
    cod=0
    for i in range(1,a+1):
        if a%i==0:
            cod+=1
    if cod==2:
        print ("Prime numbers are ",a)

for i in range(10,100):
    prm(i)