li =[12,13,14,15,156,"ayush","Shrivastava",161,True,False,161,"cybrom"]
li2 = [5,6,7,8]
#l3 = li+li2
li.extend(li2)
li.append("Ayush")
li.insert(9,99)


print(li[::-1])
print(li[0:3])
#print(li[11][2:5])
print(li[0::5])
print(li[::])
print(li.index("ayush"))
print(len(li))
#print(l3[::])