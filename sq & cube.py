a=int(input("Enter the number :- "))
b=a
r=0
rev=0
while a>0:
    r=a%10
  #  rev=rev*10+r
    a=a//10

    print(r,"sq of no. is",r*r,"cube of no. is",r*r*r)