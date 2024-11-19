file = open("num.txt",'w')
for i in range(1,11):
    file.write(str(i))
    if(i<9):
        file.write(" , ")
    if(i==9):
        file.write(" and ")    