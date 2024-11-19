file = open("abc.txt",'w')
for i in range(1,11):
    file.write(str(i))
    if(i<10):
        file.write(" , ")