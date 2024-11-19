file = open("table1.txt",'w')
num=int(input("Enter the number :- "))
for i in range(1,11):
    file.write(f"{num}*{i}={num*i}\n")