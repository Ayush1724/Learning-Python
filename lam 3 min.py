max=lambda a,b,c :a if a<b and a<c else (b if b<c else c) 
print("min ",max(5,6,7))