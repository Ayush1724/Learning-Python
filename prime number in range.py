def prm(a,b):
 for i in range(a,b):
    c=0
    for j in range(1,i+1):
     if i%j==0:
      c=c+1
    if c==2:
     print("prime number",i)
 


prm(10,100)

 


