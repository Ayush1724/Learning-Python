l=[]
l = range(1,101)
def odd(n):
    if(n%3==0 and n%5==0):
     return n
    else:
       pass

x=filter(odd,l)
print(list(x))   