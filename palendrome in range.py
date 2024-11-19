def pld(a):
    b=a
    rev=0
    while b>0:
        r=b%10
        rev=rev*10+r
        b=b//10
    if rev==a:
        print(a,"number is palindrome")    

for i in range(10,100):
    pld(i)