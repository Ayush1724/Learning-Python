def pld(a):
    rev=0
    b=a
    while a>0:
        r=a%10
        rev=rev*10+r
        a=a//10
    if rev==b:
        print("Palemdrome number is ",b)
for i in range(100,1001):
    pld(i)            