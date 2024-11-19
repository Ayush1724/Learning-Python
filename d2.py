s={1:"ayush",2:"anuj",3:"RAja"}
#s.clear()
#r=s.copy()
#r=s
r=s.setdefault (4,"ajaysir")
print("New member ",r)
#print(s.values(1))
a={2*k:len(v) for (k,v) in s.items()}
b={k:v*2 for (k,v) in s.items()}
print(b)