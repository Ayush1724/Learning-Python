li = [1,2,3,4,5,6,7,8,9]

def od(n):
    if(n%2==1):
        return n**2
    else:
        return n 
    
res =map (od,li)

print(list(res))