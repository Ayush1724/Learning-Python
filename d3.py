d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
d1={k:v*2 for k,v in d.items() if v>2 if v%2==0}
print(d1)