t1=[]
t2=[]
for i in range(1,12):
 x= int(input("Enter the T1 run of player {} :".format(i)))
 t1.append(x)

for i in range(1,12):
  y= int(input("Enter the T2 run of player {} :".format(i)))
  t2.append(x)

print("Total run of team no. 1",t1)
print("Total run of team no. 2",t2)

win = sum(t1) - sum(t2)

if(win>0):
 print("team 1 win by {} run".format(win))
elif(win<0):
 print("team 2 win by {} run".format(win))
else:
 print("draw")
  