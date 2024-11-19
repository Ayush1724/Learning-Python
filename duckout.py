t1=[]
t2=[]
c=0
d=0
for i in range(1,12):
 x= int(input("Enter the T1 run of player {} :".format(i)))
 t1.append(x)

for i in range(1,12):
  y= int(input("Enter the T2 run of player {} :".format(i)))
  t2.append(x)

for i in range(1,12):
  if t1[i]==0:
    c +=1

for i in range(1,12):
  if t2[i]==0:
    d +=1

print(c)
print(d)        
