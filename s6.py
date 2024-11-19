s="AYUSH"
i=0
sum2=0
sum=1

while i<len(s):
  sum+= ord(s[i])
  i=+1

print(sum)
t=sum
while t>10:
  while t>0:
    r=t%10
    sum2+=r  
    t=t//10
t=sum2    

print(sum2)     