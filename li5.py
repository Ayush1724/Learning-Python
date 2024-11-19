li = []

i=1
while i<=5:
    x=int(input("Enter the number :- "))
    if x in li:
        print("Value exist")
        pass
    else:
        li.append(x)
        i=i+1

print(li)




