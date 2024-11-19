li = {1,2,3,4,5,6,7,8}

def od(n):
    if(n%2==1):
        return n
    
res =filter (od,li)

print(list(res))